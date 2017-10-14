var fs  = require('fs');
var csv = require('tiny-csv');
var natural = require('natural');

var csvData = fs.readFileSync('data/example.csv', 'utf8');
var examples = csv(csvData);


var classifier = new natural.BayesClassifier();

examples.forEach(function(sample) {
        classifier.addDocument(sample.title + " type_" +sample.type , sample.isAccepted);
});

classifier.train();

console.log(classifier.getClassifications('Augmented reality architecture in the age of microservices type_Full'));