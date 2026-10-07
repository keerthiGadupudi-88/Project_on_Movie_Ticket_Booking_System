import streamlit as st
from datetime import datetime

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 25px;
}

.booking-box {
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 25px;
    margin-top: 20px;
}

.total-box {
    border: 2px solid #333;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-top: 20px;
}

.total-label {
    font-size: 18px;
    font-weight: 600;
}

.total-price {
    font-size: 32px;
    font-weight: 700;
}

.footer {
    text-align: center;
    color: #666;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# MOVIE DATA
# =========================================================

MOVIES = {
    "Avengers: Endgame": {
        "genre": "Action / Adventure",
        "duration": "3h 2m"
    },
    "Interstellar": {
        "genre": "Sci-Fi / Drama",
        "duration": "2h 49m"
    },
    "The Lion King": {
        "genre": "Animation / Adventure",
        "duration": "1h 58m"
    },
    "Inception": {
        "genre": "Sci-Fi / Thriller",
        "duration": "2h 28m"
    },
    "Spider-Man: No Way Home": {
        "genre": "Action / Superhero",
        "duration": "2h 28m"
    }
}

TICKET_PRICES = {
    "Regular": 150,
    "Premium": 250,
    "VIP": 400
}

SHOW_TIMES = [
    "10:00 AM",
    "1:30 PM",
    "4:30 PM",
    "7:30 PM",
    "10:00 PM"
]

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🎬 Movie Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your movie tickets quickly and easily</div>',
    unsafe_allow_html=True
)

# =========================================================
# CUSTOMER DETAILS
# =========================================================

st.subheader("👤 Customer Details")

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter your name"
)

# =========================================================
# MOVIE SELECTION
# =========================================================

st.subheader("🎥 Select Movie")

movie = st.selectbox(
    "Choose a movie",
    list(MOVIES.keys())
)

movie_details = MOVIES[movie]

st.info(
    f"🎬 **{movie}**  \n"
    f"Genre: {movie_details['genre']}  \n"
    f"Duration: {movie_details['duration']}"
)

# =========================================================
# SHOW TIME
# =========================================================

st.subheader("🕐 Select Show Time")

show_time = st.selectbox(
    "Choose show time",
    SHOW_TIMES
)

# =========================================================
# TICKET CATEGORY
# =========================================================

st.subheader("🎟️ Ticket Category")

ticket_type = st.radio(
    "Select ticket category",
    list(TICKET_PRICES.keys()),
    horizontal=True
)

ticket_price = TICKET_PRICES[ticket_type]

st.write(
    f"**{ticket_type} Ticket Price:** ₹{ticket_price}"
)

# =========================================================
# NUMBER OF TICKETS
# =========================================================

st.subheader("🔢 Number of Tickets")

number_of_tickets = st.number_input(
    "Select number of tickets",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

# =========================================================
# BOOK TICKETS
# =========================================================

if st.button("🎟️ Book Tickets", use_container_width=True):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not customer_name.strip():

        st.warning("⚠️ Please enter your name.")

    elif number_of_tickets < 1:

        st.warning("⚠️ Please select at least one ticket.")

    else:

        # -------------------------------------------------
        # CALCULATE TOTAL
        # -------------------------------------------------

        total_price = ticket_price * number_of_tickets

        # -------------------------------------------------
        # BOOKING SUCCESS
        # -------------------------------------------------

        st.success("🎉 Booking confirmed successfully!")

        # -------------------------------------------------
        # BOOKING SUMMARY
        # -------------------------------------------------

        st.markdown(
            '<div class="booking-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            "<h2 style='text-align:center;'>🎬 Booking Summary</h2>",
            unsafe_allow_html=True
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Customer Name**")
            st.write("**Movie**")
            st.write("**Genre**")
            st.write("**Duration**")
            st.write("**Show Time**")
            st.write("**Ticket Type**")
            st.write("**Number of Tickets**")
            st.write("**Price per Ticket**")

        with col2:
            st.write(customer_name)
            st.write(movie)
            st.write(movie_details["genre"])
            st.write(movie_details["duration"])
            st.write(show_time)
            st.write(ticket_type)
            st.write(number_of_tickets)
            st.write(f"₹{ticket_price:.2f}")

        st.divider()

        booking_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

        st.caption(
            f"Booking Date & Time: {booking_time}"
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        # -------------------------------------------------
        # TOTAL
        # -------------------------------------------------

        st.markdown(
            f"""
            <div class="total-box">
                <div class="total-label">💰 TOTAL AMOUNT</div>
                <div class="total-price">₹{total_price:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🎬 Enjoy your movie! 🍿
        <br>
        Movie Ticket Booking System
        <br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)