const genQuery = (question) => {
    const firstLine = question.split("\r\n")[0];
    const query = firstLine.startsWith("#") ? firstLine.split("#")[1] : firstLine;
    return query;
  };
  module.exports = genQuery;