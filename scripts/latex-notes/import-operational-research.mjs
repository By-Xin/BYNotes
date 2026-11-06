// Reviewed, one-note Markdown → LaTeX import. Semantic ranges are explicit;
// this is not a heuristic formatter for arbitrary notes.
import fs from 'node:fs'
import path from 'node:path'
import { createHash } from 'node:crypto'
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkMath from 'remark-math'

const dir = path.resolve('sources/deterministic-operational-research')
const source = fs.readFileSync(path.join(dir,'revised.md'),'utf8')
const reviewedSha = '78d3e3e87117c9ecfe8dd58716c227eb993de4a23d2f6b958590e3d71f909c29'
if(createHash('sha256').update(source).digest('hex')!==reviewedSha) throw Error('Source changed: re-review the correction ledger and semantic ranges before importing')
const lines = source.split('\n')
const parser = unified().use(remarkParse).use(remarkMath)
const ranges = []
function block(start,end,env,title='',strip='') { ranges.push({start,end,env,title,strip}) }
block(36,41,'defblock','一般优化模型')
block(45,62,'defblock','线性规划与标准型')
block(67,67,'defblock','凸优化问题')
block(69,69,'propositionblock')
block(76,84,'defblock','Affine and convex combinations')
block(85,85,'propositionblock','',/^\s*- \*\*Proposition\*\*: /)
block(89,104,'defblock','Hyperplane and halfspace',/^\*\*Hyperplane and halfspace\.\*\*/)
block(106,118,'defblock','Norm ball, ellipsoid',/^\*\*Norm ball, ellipsoid\.\*\*/)
block(120,128,'defblock','Polyhedron, polytope',/^\*\*Polyhedron, polytope\.\*\*/)
block(130,147,'defblock','Simplex',/^\*\*Simplex\.\*\*/)
block(150,155,'defblock','Convex cone',/^\*\*Convex cone\.\*\*/)
block(159,168,'defblock','Second-order cone')
block(169,177,'defblock','Positive semidefinite cone')
block(179,183,'defblock','Conic optimization')
block(190,196,'propositionblock','保凸运算')
block(202,206,'defblock','Affine space')
block(208,208,'thmblock','Carathéodory',/^\*\*\*Theorem\* \(Carathéodory\)\*\*: /)
block(213,220,'proof','',/^\*Proof\$~\^\\dagger\$\* /)
block(230,246,'defblock','Basic topologies')
block(249,260,'defblock','Relative interior')
block(262,268,'propositionblock','Relative interior of a convex set')
block(274,278,'thmblock','Weierstrass',/^\*\*\*Theorem\* \(Weierstrass\)\*\*: /)
block(284,284,'proof*','Proof Sketch',/^\*Proof Sketch\*: /)
block(286,295,'proof','',/^\*Proof\* /)
block(297,297,'colblock','强凸函数在闭凸集上的最优解存在且唯一',/^\*\*\*Corollary\* /)
block(305,312,'defblock','Euclidean distance and projection')
block(314,314,'thmblock','凸闭集上的投影存在唯一',/^\*\*\*Theorem\*\*\* \*\(凸闭集上的投影存在唯一\)\*: /)
block(316,352,'proof','',/^\*Proof\*\. /)
block(357,361,'thmblock','Projection variational inequality',/^\*\*\*Theorem\* \(Projection variational inequality\)\*\*: /)
block(367,391,'proof','',/^\*Proof\*\. ?/)
block(399,402,'defblock','Normal cone')
block(418,425,'propositionblock','法锥与投影')
block(433,436,'propositionblock','Polyhedral normal cone')
block(460,466,'defblock','Cones')
block(472,475,'defblock','Tangent cone')
block(486,489,'defblock','Polar cone')
block(499,502,'defblock','Dual cone')
block(504,509,'propositionblock','Dual cone properties')
block(515,523,'thmblock','Firm non-expansiveness',/^\*\*\*Theorem\* \(Firm non-expansiveness\)\*\*: /)
block(527,545,'proof','',/^\*Proof\*\./)
block(547,551,'colblock','Pythagorean theorem',/^\*\*\*Corollary\* \(Pythagorean theorem\)\*\*: /)
block(557,560,'defblock','Squared projection distance')
block(562,565,'propositionblock','平方投影距离是凸且可微的',/^\*\*\*Proposition\* /)
block(567,594,'proof','',/^\*Proof\*\. /)
block(596,608,'remarkblock','Fréchet differentiability')
block(613,616,'defblock','Proximal operator')
block(619,622,'defblock','Indicator function')
block(632,635,'defblock','Moreau envelope')
block(645,648,'exampleblock','Projection onto a halfspace',/^\*\*\*Projection onto a halfspace\*\*\*\. /)
block(650,654,'proof','',/^\*Proof\*\. /)
block(656,662,'exampleblock','Projection onto a non-negative orthant cone',/^\*\*\*Projection onto a non-negative orthant cone\*\*\*\. ?/)
block(664,668,'proof','',/^\*Proof\*\. /)
block(676,681,'defblock','Weak and strong separation')
block(686,691,'defblock','Proper separation')
block(697,700,'thmblock','Point-set separation',/^\*\*\*Theorem\* \(Point-set separation\)\*\* /)
block(705,732,'proof','',/^\*Proof\*\. */)
block(737,740,'thmblock','Finite-dimensional separation',/^\*\*\*Theorem\* \(Finite-dimensional separation\)\*\* /)
block(745,751,'remarkblock','Separation via the difference set')
block(753,763,'proof','Proof Sketch',/^\*Proof Sketch\*\. ?/)
block(765,768,'colblock','',/^\*\*\*Corollaries\*\*\*\. /)
block(772,780,'defblock','Supporting hyperplane')
block(784,784,'thmblock','Supporting hyperplane theorem',/^\*\*\*Theorem\* \(Supporting hyperplane theorem\)\*\*: /)
block(786,786,'proof*','Proof Sketch',/^\*Proof Sketch\*\. /)
block(788,804,'proof*','Proof',/^\*Proof\*\. ?/)
block(806,806,'colblock','',/^\*\*\*Corollary\*\*\*: /)
block(819,823,'defblock','Support function')
block(828,832,'propositionblock','Support function representation')
block(834,841,'exampleblock','Support functions')
block(843,848,'defblock','Exposed face',/^\*\*\*Exposed face\*\*\*\./)
block(871,873,'thmblock','Farkas lemma, standard form',/^\*\*\*Theorem\* \(Farkas lemma, standard form\)\*\* /)
block(875,887,'proof','',/^\*Proof\*\. /)
block(901,909,'exampleblock','Farkas lemma in No-arbitrage financial market',/^\*\*\*Example\* \(Farkas lemma in No-arbitrage financial market\)\*\*\. ?/)
block(915,918,'propositionblock','Some Classic Variants')
block(967,973,'exampleblock','',/^\*\*\*Example\.\*\*\* /)
block(975,997,'proof','',/^\*Proof\*\. ?/)
block(1009,1022,'defblock','Extreme points, vertices and basic feasible solutions')
block(1024,1027,'lemmablock')
block(1029,1032,'propositionblock')
block(1036,1036,'thmblock','Extreme point characterization',/^\*\*\*Theorem\*\* \(Extreme point characterization\)\*\. /)
block(1062,1064,'thmblock','Basic Solution Characterization in Standard Form',/^\*\*\*Theorem\* \(Basic Solution Characterization in Standard Form\)\*\*\./)
block(1066,1066,'defblock','Basic and non-basic variables')
block(1079,1112,'exampleblock','',/^\*Example\*\. /)
block(1164,1166,'defblock','Degeneracy')
block(1168,1171,'propositionblock','Degeneracy')
block(1191,1194,'thmblock','Existence of extreme points',/^\*\*\*Theorem\* \(Existence of extreme points\)\.\*\* /)
block(1196,1221,'proof','',/^\*Proof\*\. ?/)
block(1223,1223,'colblock')
block(1233,1234,'thmblock','Optimality of extreme points',/^\*\*\*Theorem\* \(Optimality of extreme points\)\.\*\*/)
block(1236,1240,'proof','',/^\*Proof\.\* /)
block(1244,1244,'thmblock','Optimality of extreme points',/^\*\*\*Theorem\* \(Optimality of extreme points\)\*\*\. /)
block(1246,1258,'proof*','Proof',/^\*Proof\*\. */)
block(1264,1267,'defblock','Pointed polyhedral cone')
block(1269,1276,'defblock','Recession cone')
block(1278,1278,'defblock','Extreme rays')
block(1284,1284,'thmblock','Extreme rays on standard polyhedron',/^\*\*\*Theorem\* \(Extreme rays on standard polyhedron\)\*\*\. /)
block(1286,1293,'proof','',/^\*Proof\*\. /)
block(1295,1295,'colblock')
block(1302,1310,'defblock','H- and V-representations')

const images = []; const inventory = {text:[],math:[]}
const esc = s=>s.replace(/[\\{}%&#_$~^]/g,c=>({'\\':'\\textbackslash{}','~':'\\textasciitilde{}','^':'\\textasciicircum{}'}[c]??'\\'+c))
function emit(n) {
  const children=()=>n.children.map(emit).join('')
  switch(n.type) {
    case 'root': return children()
    case 'text': inventory.text.push(n.value); return esc(n.value)
    case 'paragraph': return children()+'\n\n'
    case 'strong': return '\\textbf{'+children()+'}'
    case 'emphasis': return '\\emph{'+children()+'}'
    case 'inlineMath': inventory.math.push(n.value); return '$'+n.value+'$'
    case 'math': inventory.math.push(n.value); return '\\[\n'+n.value+'\n\\]\n\n'
    case 'heading': {
      if(n.depth===1) return '\\textbf{'+children()+'}\n\n'
      let text=children().replace(/^\d+(?:\.\d+)*\.?\s*/, '')
      return '\\'+({2:'section',3:'subsection',4:'subsubsection'}[n.depth])+'{'+text+'}\n\n'
    }
    case 'list': return '\\begin{'+(n.ordered?'enumerate':'itemize')+'}\n'+children()+'\\end{'+(n.ordered?'enumerate':'itemize')+'}\n\n'
    case 'listItem': return '\\item {}'+children()+'\n'
    case 'blockquote': if(n.children[0]?.children?.[0]?.value?.startsWith('[!Note]')) n.children[0].children[0].value=n.children[0].children[0].value.replace('[!Note]','Note.'); return '\\begin{quote}\n'+children()+'\\end{quote}\n\n'
    case 'html': {
      if(n.value.startsWith('<!--')) return n.value.split('\n').map(l=>'% '+l).join('\n')+'\n'
      const m=n.value.trim().match(/^<img src="(https:\/\/raw\.githubusercontent\.com\/By-Xin\/Blog-figs\/main\/[^"]+)" width="(\d+)%">$/)
      if(!m) throw Error('Unreviewed HTML: '+n.value)
      const name=path.basename(m[1]); images.push({url:m[1],file:'figures/'+name,width:Number(m[2])/100})
      return '\\begin{center}\n\\includegraphics[width='+Number(m[2])/100+'\\linewidth]{figures/'+name+'}\n\\end{center}\n\n'
    }
    case 'break': return '\n'
    default: throw Error('Unreviewed Markdown node '+n.type+' '+JSON.stringify(n).slice(0,400))
  }
}
function convert(s) { return emit(parser.parse(s)) }
let body='', cursor=1
for (const b of ranges) {
  if(b.start<cursor) throw Error('Overlapping semantic ranges')
  body+=convert(lines.slice(cursor-1,b.start-1).join('\n'))
  let chunk=lines.slice(b.start-1,b.end).join('\n')
  if(b.strip) { if(!b.strip.test(chunk)) throw Error('Prefix mismatch '+b.start); chunk=chunk.replace(b.strip,b.start===213?'$~^\\dagger$ ':'') }
  if(b.env==='proof') {
    if(!chunk.includes('$\\square$')) throw Error('Missing QED '+b.start)
    chunk=chunk.replace('$\\square$','')
  }
  if(b.env==='remarkblock') chunk=chunk.replace(/^> ?/gm,'')
  if([297,562].includes(b.start)) chunk=chunk.replace(']**',']')
  if(!chunk.trim()) throw Error('Empty semantic block '+b.start)
  if(chunk.split('\n').filter(l=>l.trim()==='$$').length%2) throw Error('Math fence crosses semantic block '+b.start)
  body+='\n% Source Markdown lines '+b.start+'–'+b.end+'\n\\begin{'+b.env+'}'+(b.title?'[{'+esc(b.title)+'}]':'{}')+'\n'+convert(chunk)+'\\end{'+b.env+'}\n\n'
  cursor=b.end+1
}
body+=convert(lines.slice(cursor-1).join('\n'))
// Independently compare the complete Markdown tree with the segmented import.
// Only the fifteen explicit QED tokens move from math into proof endings.
const originalInventory = {text:[],math:[]}
function collect(n) {
  if(n.type==='text') originalInventory.text.push(n.value)
  if(['math','inlineMath'].includes(n.type)) originalInventory.math.push(n.value)
  n.children?.forEach(collect)
}
collect(parser.parse(source))
const mathNormalize=s=>s.replace(/\s+/g,'')
const expectedMath=originalInventory.math.filter(s=>s.trim()!=='\\square').map(mathNormalize)
if(JSON.stringify(expectedMath)!==JSON.stringify(inventory.math.map(mathNormalize))) throw Error('Math lost, changed or reordered during import')
const textNormalize=s=>s.replace(/[^\p{L}\p{N}]/gu,'')
const retainedText=textNormalize(inventory.text.join(' ')+ranges.map(b=>b.title).join(' '))
const missingText=originalInventory.text.map(textNormalize).filter(s=>s.length>=15&&!retainedText.includes(s))
if(missingText.length) throw Error('Prose lost during import: '+missingText.join('\n'))
fs.writeFileSync(path.join(dir,'import-audit.json'),JSON.stringify({passed:true,math_preserved_in_order:expectedMath.length,qed_preserved_as_proof_endings:originalInventory.math.length-expectedMath.length,prose_fragments_checked:originalInventory.text.filter(s=>textNormalize(s).length>=15).length,semantic_blocks:ranges.length,image_occurrences:images.length},null,2)+'\n')
fs.writeFileSync(path.join(dir,'body.tex'),body)
if(fs.existsSync(path.join(dir,'template.tex'))) fs.writeFileSync(path.join(dir,'main.tex'),fs.readFileSync(path.join(dir,'template.tex'),'utf8')+'\\begin{document}\n\\maketitle\n'+body+'\n\\end{document}\n')
fs.writeFileSync(path.join(dir,'structure.json'),JSON.stringify({revised_sha256:createHash('sha256').update(source).digest('hex'),blocks:ranges.map(({strip,...b})=>b),images,inventory},null,2)+'\n')
console.log('Imported',ranges.length,'semantic blocks;',images.length,'image occurrences;',inventory.math.length,'math expressions')
