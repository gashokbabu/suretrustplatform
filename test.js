// function hello()
// {
//     fetch("http://suretrustplatform.herokuapp.com/users", {
//     method: "POST",
//     headers: {
//     "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//     email: "pip@gmail.com",
//     password: "django@999",
//     name: "pip",
//     gender: "male",
//     phone: 7589859,
//     }),
// })
//     .then((response) => response.json())
//     .then((data) => {
//     console.log("data", data);
//     if (typeof data.id === "undefined") {
//         console.log("error")
//     }
//     })

// }

// hello()
      




var requestOptions = {
  method: 'POST',
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({
    email: "pip@gmail.com",
    password: "django@999",
    name: "pip",
    gender: "male",
    phone: 7589859,
    }),
  redirect: 'follow'
};

fetch("https://suretrustplatform.herokuapp.com/users/", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));