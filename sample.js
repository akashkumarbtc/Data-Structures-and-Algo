const p1 = new Promise((resolve, reject) =>{
    setTimeout(() => {
        const result = false;
        if (result) resolve("Promise resolved");
        else reject("Promise rejected");
    }, 1000)
})

p1.then((res) =>{
    console.log(res)
}).catch((err) =>{
    console.log(err)
})