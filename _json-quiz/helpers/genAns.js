const correctAnswer = require("./correctAns");

const genAns = (question) => {
  let options;
  let correctAns;
  if (question.split("```").length === 1) {
    let answers = question.split("\r\n").slice(1).join("\r\n");
    if (!answers) answers = question.split("\n").slice(1).join("\n");
    correctAns = correctAnswer(answers);
    options = genOptions(question);
  }

  if (question.split("```").length === 3) {
    let answers = question.split("```")[2].split("\r\n").join(""); // goes to the last one

    if (!answers.includes("[x]")) {
      answers = question.split("```")[1].split("\r\n").join("");
    }
    correctAns = correctAnswer(answers);
    options = genOptions(question);
  }

  if (question.split("```").length === 5) {
    const answers = question.split("```")[4].split("\r\n").join(""); // goes to the last one
    correctAns = correctAnswer(answers);
    options = genOptions(question);
  }

  if (question.split("```").length === 9) {
    const answers = question.split("\r\n").slice(1).join("");
    correctAns = correctAnswer(answers);
    options = genOptions(question);
  }

  if (question.split("```").length === 11) {
    const answers = question.split("```").slice(2).join("");
    correctAns = correctAnswer(answers);
    options = genOptions(question);
  }
  if (!options || !options[options.length - 1]) {
    return { options, correctAns };
  }
  if (options[options.length - 1].includes("[Ref")) {
    options[options.length - 1] = options[options.length - 1].split("[Ref")[0];
  }

  if (options[options.length - 1].includes("Source:")) {
    options[options.length - 1] =
      options[options.length - 1].split(/\[?Source/)[0];
  }

  return { options, correctAns };
};

const genOptions = (question) => {
  let options = question
    .split("\r\n")
    .slice(1)
    .join("\r\n")
    .split(/- \[ ?x?\]/)
    .slice(1);

  if (options.length === 0) {
    options = question
      .split("\r\n")
      .slice(1)
      .join("\r\n")
      .split(/\[?x?\]/)
      .slice(1);
  }
  return options;
};

module.exports = genAns;