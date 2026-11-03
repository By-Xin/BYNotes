import unittest
from convert import Parser, Renderer, annotate, uncomment


def render(source):
    nodes = Parser(uncomment(source)).parse()
    renderer = Renderer(annotate(nodes), "./assets")
    return renderer, renderer.flow(nodes)


class FidelityTests(unittest.TestCase):
    def test_comments_preserve_escaped_percent(self):
        self.assertEqual(uncomment("a\\%b%comment\nc"), "a\\%b\nc")
        self.assertEqual(uncomment("a\\\\%comment\nc"), "a\\\\\nc")

    def test_nested_note_and_math_preserve_content(self):
        renderer, output = render(r"Before \footnote{Deep \textbf{nested {words}} $a_{b_{c}}$} after")
        self.assertEqual(renderer.math[0]["tex"], r"a_{b_{c}}")
        self.assertIn("nested words", renderer.footnotes[0][0][1])
        self.assertIn("Before", output)
        self.assertIn("after", output)

    def test_final_table_cell_renders_math_once(self):
        renderer, output = render(r"\begin{tabular}{cc}a & b \\ c & $x$\end{tabular}")
        self.assertEqual(len(renderer.math), 1)
        self.assertEqual(output.count("@@MATH0@@"), 1)

    def test_reference_resolves_forward_and_counter_resets(self):
        renderer, output = render(r"\section{A}\subsection{B}\ref{last}\begin{axiomblock}a\end{axiomblock}\begin{axiomblock}\label{last}b\end{axiomblock}\subsection{C}\begin{axiomblock}c\end{axiomblock}")
        self.assertEqual(renderer.labels["last"][0], "1.1.2")
        self.assertIn("Axiom 1.2.1", output)

    def test_nested_proof_is_expanded(self):
        renderer, output = render(r"\begin{thmblock}Claim\begin{proof}Argument\end{proof}\end{thmblock}")
        self.assertIn('<details class="latex-proof" open>', output)
        self.assertEqual(renderer.census["proof"], 1)

    def test_mathematical_diamond_survives(self):
        renderer, _ = render(r"Let $\diamond$ denote an operation.")
        self.assertEqual(renderer.math[0]["tex"], r"\diamond")

    def test_unhandled_semantics_fail(self):
        for source in (r"\cite{paper}", r"\setcounter{section}{5}", r"\renewcommand{\R}{X}", r"\begin{enumerate}[a)]\item x\end{enumerate}", r"\begin{itemize}\item[Special]x\end{itemize}"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                render(source)

    def test_unclosed_group_and_environment_fail(self):
        for source in (r"\textbf{oops", r"\begin{proof}unfinished"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                render(source)


if __name__ == "__main__":
    unittest.main()
