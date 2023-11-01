const fs = require("fs");

// List of words to generate a random 12-word seed phrase
const words = [
 // strong words
];

function generateSeedPhrase(numberOfPhrases) {
    // generate 
  }
  
  
  const numberOfPhrasesToGenerate = aa;
  const uniqueSeedPhrases = generateSeedPhrase(numberOfPhrasesToGenerate);
  
  // Convert seed phrases to a text format
  const dataToWrite = uniqueSeedPhrases
    .map((seedPhrase) => `${seedPhrase}`)
    .join("\n");
  
  fs.writeFile("a.txt", dataToWrite, (err) => {
    // function 
  }
  );