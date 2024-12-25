const fs = require("fs");
const path = require("path");

const directoryPath = path.join(__dirname, "./images"); // Path to the images folder
const outputPath = path.join(__dirname, "images.json"); // Path to save images.json

fs.readdir(directoryPath, (err, files) => {
  if (err) {
    return console.error("Unable to scan directory:", err);
  }

  // Filter image files
  const imageFiles = files.filter((file) =>
    file.match(/\.(jpg|jpeg|png|gif|webp)$/i)
  );

  // Write to images.json
  fs.writeFile(outputPath, JSON.stringify(imageFiles, null, 2), (err) => {
    if (err) {
      console.error("Error writing JSON file:", err);
    } else {
      console.log("images.json file created successfully!");
    }
  });
});
