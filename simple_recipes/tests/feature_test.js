const TestRunner = require('test-runner')
var feature = require('./feature.js')
const runner = new TestRunner()

runner.test('text feature', function(){
    var X = ['one two three', 'four five six']
	var cv = feature.CountVectorizer();
    var output = cv.fit_transform(X);
    if (output.length != 2){
        console.log(output.length)
        throw new Error(output);
    }
    if (output[0].length != 6){
        console.log(output[0].length)
        throw new Error(output);
    }
})

runner.test('text cleaner', function(){
	var tc = feature.TextCleaner();
    var output = tc.transform(['hello? world!']);
    if (output[0] != 'hello world'){
        throw new Error(output);
    }
})

runner.test('text ohe', function(){
	var tc = feature.OneHotEncoder();
    var output = tc.fit_transform([['cat', 1], ['dog', 0]]);
    if (output[0].length != 4){
        console.log(output[0])
        throw new Error(output);
    }
})