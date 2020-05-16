import * as fs from 'fs';
import { promisify } from 'util';

const readFile = promisify(fs.readFile)

async function main() {
  const buf: Buffer = await readFile('./a.txt')
  new File([buf])
}