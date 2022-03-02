#!/usr/bin/node
// JS Script
let fs = require('fs');
let text1 = fs.readFileSync(process.argv[2], 'utf-8');
let text2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.appendFile(process.argv[4], text1.concat(text2).trim());
fs.appendFile(process.argv[4], '\n');
