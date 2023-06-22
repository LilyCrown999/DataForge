


// // var apiUrl = 'http://127.0.0.1:8000/gene'
// var apiUrl = 'http://127.0.0.1:8000/generate'
// var Data = {
//     "id" : "id",
//     "age" : "number (12-16)",
//     "amount": "number (100-200)",
//     "city" : "city",
//     "state" : "state",
//     "country" : "country",
//     "First name":  "name",
//     "Last name": "name",
//     "Gender": "gender"
// }

// // fetch(apiUrl, {
// //     method: "POST",
// //     body: Data
// // })
// // .then(response => response.json())
// // .then(data => {
// //     // API response handling
// //     console.log(data)
// // })
// // .catch(error => console.error(error));

// // Function to handle the form submission
// function fetch_url() {

//         // Make POST request to the API
//         var ff = fetch(apiUrl, {
//             method: "POST",
//             body: Data
//         })

//         console.log(ff)


//         // .then(response => {
//         //     data = response.json()
//         //     console.log(data)
//         // })
//         // // .then(data => {
//         // //     // API response handling
//         // //     console.log(data)
//         // // })
//         // .catch(error => console.error(error));

//     }

// fetch_url()

var apiUrl = 'http://127.0.0.1:8000/generate';

var Data = {
    "id" : "id",
    "age" : "number (12-16)",
    "amount": "number (100 - 20000)",
    "city" : "city",
    "state" : "state",
    "country" : "country",
    "First name":  "name",
    "Last name": "name",
    "Gender": "gender"
}



function fetch_url() {
    // Convert Data to JSON string
    var jsonData = JSON.stringify(Data);

    var headers = {
        'Content-Type': 'application/json',
        'mode': 'csv',
        'line': 1000
    };

    // Make POST request to the API
    fetch(apiUrl, {
        method: "POST",
        body: jsonData,
        headers: headers
    })
    .then(response => response.json())
    .then(data => {
        // API response handling
        console.log(data);
    })
    .catch(error => console.error(error));
}

fetch_url();
