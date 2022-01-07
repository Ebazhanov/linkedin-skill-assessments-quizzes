// const mainScript = re

// fs.readdirSync(`../`).map((fileOrDir) => {
//     const stats = fs.statSync(`../${fileOrDir}`)
//     if (!stats.isFile() && !fileOrDir.startsWith(".") && !fileOrDir.startsWith("_")) {
//         try {
//             const content = fs.readFileSync(`../${fileOrDir}/${fileOrDir}-quiz.md`)
//             // console.log(content.toString())
            
//         }
//         catch(err) {
//             console.log(`could not read file: ${fileOrDir}/${fileOrDir} `)
//         }
//     }
// })