// Entry point for the 20 November 2026 world-news image.
// Copies the pre-drawn front page (entry.png, next to this file)
// into the grader's output directory. No network, no randomness:
// the same input bytes always produce the same output bytes.
import { copyFileSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(targetDir, "entry.png");

mkdirSync(targetDir, { recursive: true });
copyFileSync(source, target);

const bytes = statSync(target).size;
const sourceBytes = readFileSync(source).length;
console.log(`wrote ${target} (${bytes} bytes, source ${sourceBytes} bytes)`);
