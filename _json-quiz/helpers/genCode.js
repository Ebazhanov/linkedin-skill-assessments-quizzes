const genCode = (question, i) => {
    let code;
    const splittedCode = question.split("```");

    if (question.includes("(images")) return "image not support yet";
    if (splittedCode === 1) return null;
    if (splittedCode.length === 3) {
      return question.split("```")[1].split("\r\n").join("").includes("[x]")
        ? null
        : question.split("```")[1];
    }
    if (splittedCode.length === 5) {
      return question.split("```").slice(1, 4).join("").includes("[x]")
        ? null
        : question.split("```").slice(1, 4).join("");
    }
    if (splittedCode.length === 9) {
      return null;
    }
    if (splittedCode.length === 11) {
      return splittedCode[1];
    }
  };
  
  module.exports = genCode;