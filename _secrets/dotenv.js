require('dotenv').config({path: '/home/tirth/vscode/Mort-Pages-Personal/Keys.env'});

const API_KEY = process.env.API_KEY;
const DB_KEY = process.env.DB_KEY;

console.log("API_KEY:" + API_KEY);
console.log("DB_KEY:" + DB_KEY);