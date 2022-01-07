const path = require("path");
const fs = require("fs");
const genQuery = require("./helpers/genQuery");
const genAns = require("./helpers/genAns");
const genCode = require("./helpers/genCode");

let totalQuestionsInsert=0;
let totalQuestionsNotInserted=0;

const filesToConvert = fs.readdirSync("../").filter((fileOrDir) => {
    const stats = fs.statSync(`../${fileOrDir}`)
    return (!stats.isFile() && !fileOrDir.startsWith(".") && !fileOrDir.startsWith("_")) 
})

filesToConvert.map((fileName) => {
  const file = fs
    .readFileSync(`../${fileName}/${fileName}-quiz.md`)
    .toString()
    .split("###");

  const questions = file.slice(1).map((question) => {
    const query = genQuery(question);
    const code = genCode(question);
    const { options, correctAns } = genAns(question);
    if (!options || !correctAns || code === "image not support yet") {
        totalQuestionsNotInserted+=1
        return
    };
    return {
      query,
      code,
      options,
      correctAns,
    };
  });
  const inserted = questions.reduce((a, q) => (q ? a + 1 : a), 0);
  totalQuestionsInsert+=inserted
  console.log(`${fileName}.json: ${inserted} Question inserted`);
  fs.writeFileSync(`./questions/${fileName}.json`, JSON.stringify(questions));
});

console.log(`${totalQuestionsInsert} questions inserted \r\n ${totalQuestionsNotInserted} questions not inserted`)