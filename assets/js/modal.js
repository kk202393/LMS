const sendOTP = () => {
    try {
        const PhoneNumber = document.getElementById("id_PhoneNumber").value
        const OtpCount = Math.floor(Math.random() * (12 - 6 + 1)) + 6
        console.log("customer phone number", PhoneNumber)
        console.log(Math.floor(Math.random() * (12 - 6 + 1)) + 6)
        $.ajax({
            type: "GET",
            url: "/sendOTP",
            data: {
                Phone_Number: PhoneNumber,
                Otp_Count: OtpCount
            },
            success: function (data) {
                Swal.fire({
                    icon: 'success',
                    title: 'Great!',
                    text: `OTP has been send to ${PhoneNumber}`,
                });
                document.getElementById("OTPNUMBER").value = Number(data.OTP);
            },
            error: function (xhr, status, error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...!',
                    text: `${error}`,
                });
            }
        })
    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...!',
            text: `Something Went Wrong`,
        });
    }

}




const OTPverify = () => {
    try {
        if (Number(document.getElementById("OTPVALUE").value) === Number(document.getElementById("OTPNUMBER").value)) {
            Swal.fire({
                icon: 'success',
                title: 'Great!',
                text: 'Your OTP is correct',
            });
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Oops...!',
                text: 'Your Enter Wrong OTP',
            });
        }

    } catch (error) {
        console.log("Something Went Wrong")
    }
}




