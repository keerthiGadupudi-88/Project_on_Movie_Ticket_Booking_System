# 🎬 Movie Ticket Booking System

A simple and beginner-friendly **Movie Ticket Booking System** built using **Python and Streamlit**.

The application allows users to select a movie, choose a show time, select a ticket category, enter the number of tickets, and calculate the total ticket price.

## 🚀 Features

* 🎬 Select a movie
* 🕐 Select show time
* 🎟️ Select ticket category
* 🔢 Select number of tickets
* 💰 Calculate total ticket price
* 👤 Enter customer name
* 🧾 Display booking summary
* 📅 Display booking date and time
* 📱 Mobile-friendly interface
* ✅ Input validation
* ✨ Clean and simple UI

## 🛠️ Technologies Used

* Python
* Streamlit

## 📁 Project Structure

```text
movie-ticket-booking/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎟️ Ticket Categories

| Ticket Type | Price |
| ----------- | ----: |
| Regular     |  ₹150 |
| Premium     |  ₹250 |
| VIP         |  ₹400 |

## 🎥 Available Movies

The application currently includes:

* Avengers: Endgame
* Interstellar
* The Lion King
* Inception
* Spider-Man: No Way Home

Each movie displays its genre and duration.

## 🧮 Price Calculation

The total price is calculated using:

```text
Total Price = Ticket Price × Number of Tickets
```

### Example

If the user selects:

```text
Ticket Type = Premium
Ticket Price = ₹250
Number of Tickets = 3
```

Then:

```text
Total Price = ₹250 × 3

Total Price = ₹750
```

## 💻 Run the Project Locally

### Step 1: Open the project folder

```bash
cd movie-ticket-booking
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

Usually the local URL is:

```text
http://localhost:8501
```

## 🧪 Testing

The following test cases should be performed before deployment.

### Test Case 1: Empty Customer Name

Leave the customer name empty and click:

```text
Book Tickets
```

Expected result:

```text
Please enter your name.
```

### Test Case 2: Movie Selection

Select each movie one by one.

Expected result:

* Movie name changes
* Genre changes correctly
* Duration changes correctly

### Test Case 3: Ticket Category

Test:

```text
Regular
Premium
VIP
```

Expected prices:

```text
Regular = ₹150
Premium = ₹250
VIP = ₹400
```

### Test Case 4: Number of Tickets

Test different quantities:

```text
1
2
5
10
```

The total should change accordingly.

### Test Case 5: Total Calculation

Example:

```text
VIP
₹400
3 tickets
```

Expected:

```text
₹400 × 3 = ₹1200
```

### Test Case 6: Show Time

Test every available show:

```text
10:00 AM
1:30 PM
4:30 PM
7:30 PM
10:00 PM
```

Expected result:

The selected show time should appear in the booking summary.

### Test Case 7: Booking Summary

After clicking **Book Tickets**, verify that the summary contains:

* Customer name
* Movie
* Genre
* Duration
* Show time
* Ticket type
* Number of tickets
* Price per ticket
* Total amount

### Test Case 8: Mobile Testing

Open the deployed application on a smartphone.

Check:

* Text is readable
* Buttons are visible
* Movie selection works
* Ticket selection works
* Number input works
* Booking summary is readable
* Total amount is visible
* No important content is cut off

## 🚀 Upload to GitHub

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Initial commit - Movie Ticket Booking System"
```

Rename the branch:

```bash
git branch -M main
```

Add the GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push the project:

```bash
git push -u origin main
```

## ☁️ Streamlit Community Cloud Deployment

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in using GitHub.
4. Click **Create app**.
5. Select your GitHub repository.
6. Select the `main` branch.
7. Select `app.py` as the main file.
8. Click **Deploy**.

Streamlit will install the dependencies from:

```text
requirements.txt
```

After deployment, Streamlit will provide a public URL.

## 📱 Mobile Testing

Open the deployed URL on a smartphone.

Test:

1. Enter customer name.
2. Select a movie.
3. Select show time.
4. Select ticket category.
5. Select number of tickets.
6. Click **Book Tickets**.
7. Verify the booking summary.
8. Verify the total price.

## 🔮 Future Improvements

Possible future features:

* 💺 Seat selection
* 🏢 Multiple theatres
* 📅 Movie date selection
* 💳 Payment method
* 🎫 Generate digital ticket
* 📄 Download ticket as PDF
* 📧 Email confirmation
* 🔢 Generate booking ID
* 🎞️ Add movie posters
* 🔐 Admin dashboard

## 👨‍💻 Author

Movie Ticket Booking System built using Python and Streamlit.
