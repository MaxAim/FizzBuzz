const words = {3 : "Fizz", 5 : "Buzz"};
for (let i = 1; i <= 100; i++) {
    let result = "";
    for (const key in words) {
        if(!(i % key)){
            result += words[key];
        }
    }
    console.log(result ? result : i);
}
