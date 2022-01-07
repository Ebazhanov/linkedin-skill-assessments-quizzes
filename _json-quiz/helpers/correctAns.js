const correctAns = (answers) => {
    let ans = answers
      .split(/- \[/)
      .reduce((a, c, i) => (c.startsWith("x") ? i : a), 0);
    if (ans === 0)
      ans = answers
        .split(/\[/)
        .reduce((a, c, i) => (c.startsWith("x") ? i : a), 0);
    return ans;
  };
  
  module.exports = correctAns;