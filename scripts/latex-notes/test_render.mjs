import { test } from 'node:test'
import assert from 'node:assert/strict'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { execFileSync } from 'node:child_process'

test('web math keeps compact inline layout and explicit author styles', () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'bynotes-inline-'))
  try {
    const math = [{tex:'\\sum_{i=1}^n x_i',display:false},{tex:'\\displaystyle \\frac{a}{b}',display:false},{tex:'\\int_0^1 x\\,dx',display:true}]
    fs.writeFileSync(path.join(dir,'input.json'), JSON.stringify({html:'<p>@@MATH0@@ @@MATH1@@</p>@@MATH2@@',math,headings:[],macros:{},census:{},labels:{}}))
    fs.writeFileSync(path.join(dir,'meta.json'), JSON.stringify({title:'Fixture',byline:'BYNotes',asset_slug:'assets',slug:'fixture',date:'2026-11-14',tags:[]}))
    execFileSync(process.execPath, [path.resolve('scripts/latex-notes/render.mjs'),path.join(dir,'input.json'),path.join(dir,'out.md'),path.join(dir,'meta.json')])
    const output=fs.readFileSync(path.join(dir,'out.md'),'utf8')
    const annotations=[...output.matchAll(/<annotation encoding="application\/x-tex">(.*?)<\/annotation>/gs)].map(m=>m[1])
    assert.deepEqual(annotations,math.map(m=>m.tex))
    assert.equal((output.match(/class="latex-inline-math"/g)||[]).length,2)
    assert.equal((output.match(/class="katex-display"/g)||[]).length,1)
  } finally { fs.rmSync(dir,{recursive:true,force:true}) }
})
