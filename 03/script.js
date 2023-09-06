// Get form and error element
const infoForm = document.getElementById("infoForm");
const errorContainer = document.getElementById("errorContainer");
const errorText = document.getElementById("errorText");

// Function to validate the form
function validateForm(event) {
    event.preventDefault();

    // Get form values
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const email = document.getElementById("email").value;
    const phone = document.getElementById("phone").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const gender = document.getElementById("gender").value;
    const birthdate = document.getElementById("birthdate").value;

    // Regular expressions for validation
    const nameRegex = /^[a-zA-Z\s]*$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^[0-9]{10}$/;

    // Validate password and confirm password
    if (password !== confirmPassword) {
        errorText.textContent = "Passwords do not match.";
    } else if (!nameRegex.test(firstName) || !nameRegex.test(lastName)) {
        errorText.textContent = "First Name and Last Name should contain only alphabets and spaces.";
    } else if (!firstName || !lastName || !email || !phone || !password || !confirmPassword || !gender || !birthdate) {
        errorText.textContent = "All fields are required.";
    } else if (!email.match(emailRegex)) {
        errorText.textContent = "Invalid email address.";
    } else if (!phone.match(phoneRegex)) {
        errorText.textContent = "Invalid phone number (10 digits only).";
    } else {
        // Form is valid, you can submit it to a server here
        errorText.textContent = "";
        alert("Form submitted successfully!");
    }
}

// Add form submit event listener
infoForm.addEventListener("submit", validateForm);