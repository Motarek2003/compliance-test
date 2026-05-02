// Minimal JavaScript source so CodeQL has something to analyze.

function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet("CloudSentry"));

module.exports = { greet };
