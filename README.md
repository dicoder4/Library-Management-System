# Library Management System (LMS) with MongoDB

## **Overview**
The Library Management System (LMS) is a full-stack web application designed to simplify library operations. It enables librarians to manage books and users while providing users with an intuitive interface to search, borrow, and return books. The backend uses Flask and MongoDB, while the frontend is powered by React.js.

---

## **Features**

1. **Book Management**
   - Add, update, or delete books.
   - Search books by title, author, or ISBN.

2. **User Management**
   - User registration and login.
   - View and manage user borrowing records.

3. **Borrowing and Returning**
   - Borrow books and update availability.
   - Return books and handle overdue notifications.

4. **Authentication**
   - JWT-based authentication for secure access.
   - Role-based permissions for librarians and users.

5. **Responsive Design**
   - Interactive UI built with React.js and Material-UI.

---

## **Technology Stack**

### **Backend**
- Flask (Python)
- MongoDB
- Flask-JWT-Extended

### **Frontend**
- React.js
- Material-UI

### **Other Tools**
- GitHub for version control
- Postman for API testing

---

## **Project Structure**

```
library-management-system/
├── backend/                 # Flask backend
│   ├── app.py               # Main backend entry point
│   ├── models/              # Database models
│   │   ├── book_model.py    # MongoDB schema for books
│   │   ├── user_model.py    # MongoDB schema for users
│   ├── routes/              # API routes
│   │   ├── book_routes.py   # Book-related endpoints
│   │   ├── user_routes.py   # User-related endpoints
│   ├── services/            # Business logic
│   │   ├── book_service.py  # Book-related logic
│   │   ├── user_service.py  # User-related logic
│   ├── requirements.txt     # Backend dependencies
│   ├── config.py            # MongoDB configuration
│   └── .env                 # Environment variables for sensitive info
├── frontend/                # React.js frontend
│   ├── public/              # Static files
│   ├── src/                 # Source code
│   │   ├── components/      # React components
│   │   │   ├── AddBook.js   # Add book form
│   │   │   ├── BookList.js  # Display books
│   │   │   ├── BorrowBook.js# Borrow book feature
│   │   ├── pages/           # Main pages
│   │   │   ├── Home.js      # Homepage
│   │   │   ├── Admin.js     # Admin dashboard
│   │   └── App.js           # Main entry point for React
│   ├── package.json         # Frontend dependencies
│   └── .env                 # API base URL for React
└── README.md                # Project documentation
```

---

## **Setup Instructions**

### **Backend Setup**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd library-management-system/backend
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the `backend/` directory with the following content:
     ```env
     MONGO_URI=<your-mongodb-uri>
     SECRET_KEY=<your-secret-key>
     ```

5. **Run the Server**:
   ```bash
   flask run
   ```

The backend will be accessible at `http://127.0.0.1:5000`.

---

### **Frontend Setup**

1. **Navigate to Frontend Directory**:
   ```bash
   cd library-management-system/frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Environment Variables**:
   - Create a `.env` file in the `frontend/` directory with the following content:
     ```env
     REACT_APP_API_BASE_URL=http://127.0.0.1:5000
     ```

4. **Start the Frontend Server**:
   ```bash
   npm start
   ```

The frontend will be accessible at `http://localhost:3000`.

---

## **API Endpoints**

### **Authentication**
- `POST /api/login` - User login and JWT generation.

### **Books**
- `GET /api/books/` - Retrieve all books.
- `POST /api/books/` - Add a new book.
- `PUT /api/books/<book_id>` - Update book details.
- `DELETE /api/books/<book_id>` - Delete a book.

### **Users**
- `GET /api/users/` - Retrieve all users (Admin only).
- `POST /api/users/` - Register a new user.
- `GET /api/users/<user_id>` - Get user details.

---

## **Contribution Guidelines**

1. **Branch Naming**:
   - `feature/<feature-name>`: For new features.
   - `bugfix/<bug-name>`: For bug fixes.

2. **Commit Messages**:
   - Use clear and descriptive messages (e.g., `Added book search functionality`).

3. **Pull Requests**:
   - Ensure all tests pass before creating a PR.
   - Provide a clear description of changes in the PR.

---

## **Future Enhancements**
1. Implement fine calculation for overdue books.
2. Add email notifications for due dates and overdue fines.
3. Integrate advanced role-based permissions for admin and user access.
4. Deploy the application on a cloud platform (e.g., AWS, Heroku).

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For any issues or contributions, feel free to reach out via the GitHub repository or email at `contact@example.com`.

