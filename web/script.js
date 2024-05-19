function calculate(operation) {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please fill in both numbers!");
        return;
    }

    fetch(`/calculate?operation=${operation}&num1=${num1}&num2=${num2}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
            } else {
                alert(`The result is ${data.result}`);
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            alert("An error occurred. Please try again.");
        });
}
