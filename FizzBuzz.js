var num = 0
var result = ""
words = {3:"Fizz",5:"Buzz"}
const FizzBuzz = () => {
	if (num < 100){
    result = ""
    num++
	for (key in words){
        if (num % key === 0){
            result = result + words[key]
        }
    }
    if(result === ""){
    	result = num
    }
		console.log(result)
    FizzBuzz()
  }
  else{
    console.log("Finished")
  }
}
FizzBuzz()
