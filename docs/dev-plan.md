# **Development Roadmap**

## **📍 Project Overview**
The **Stock Scanner** is a GUI-based tool that allows a user to log in via the **Charles Schwab API**, filter stocks based on specific criteria, and view results in a scrollable, interactive interface.  

- **Tech Stack:** Python, CustomTkinter, Requests, Keyring  
- **Authentication:** OAuth 2.0 with secure token storage  
- **Data Source:** Real-time stock data from the API (no local database)  
- **Filtering Criteria:** Price, stock age, options availability, fundamental data  
- **Deployment Goal:** A fully functioning stock scanner with an optimized user experience  

---

## **📌 AI Agent Responsibilities & Git Branches**
Each AI agent works in a **dedicated branch** to ensure smooth collaboration.  

| **AI Agent**            | **Git Branch**  | **Markdown File**          | **Responsibilities** |
|-------------------------|----------------|----------------------------|----------------------|
| **Project Manager AI**  | `main`         | `docs/dev-plan.md`         | Oversee development, update roadmap |
| **Lead Developer AI**   | `dev`          | `docs/lead-dev.md`         | Manage the dev branch, oversee merges |
| **Feature Developer AI**| `feature/*`    | `docs/feature-dev.md`      | Implement new features |
| **Code Review AI**      | `bugfix/*`     | `docs/code-review.md`      | Review PRs, enforce coding standards |
| **Optimization AI**     | `optimize/*`   | `docs/optimization.md`     | Improve performance & efficiency |
| **Automated Testing AI**| `test/*`       | `docs/testing.md`          | Create & run tests, report failures |
| **Deployment AI**       | `deploy/*`     | `docs/deployment.md`       | Handle production deployment |
| **Documentation AI**    | `docs/`        | `docs/docs.md`             | Maintain clear & updated documentation |

---

## **📌 Phased Development Strategy**
Development is divided into structured **phases**, ensuring smooth progress.

### **🔹 Phase 1: API Integration (Week 1-2)**
✔️ Study **Charles Schwab API** documentation  
✔️ Implement **OAuth 2.0 authentication**  
✔️ Store tokens securely using **Keyring**  
✔️ Test API authentication flow  

⏩ **Responsible Agents:**  
- **Feature Developer AI** → Implements authentication  
- **Automated Testing AI** → Validates login behavior  

---

### **🔹 Phase 2: Stock Scanner Core (Week 3-4)**
✔️ Implement API calls to fetch **stock data**  
✔️ Develop stock filtering logic for:  
  - ✅ **Price range**  
  - ✅ **Stock age (based on icon date)**  
  - ✅ **Weekly options contracts**  
  - ✅ **Fundamental data** (PE, PS, revenue, debt, free cash flow)  
✔️ Implement a **manual refresh** button  

⏩ **Responsible Agents:**  
- **Feature Developer AI** → Implements scanner logic  
- **Automated Testing AI** → Writes unit tests for filtering  
- **Code Review AI** → Ensures logic efficiency  

---

### **🔹 Phase 3: GUI Development (Week 5-6)**
✔️ Design **sidebar for filtering options**  
✔️ Implement **scrollable stock list** with:  
  - ✅ Stock name  
  - ✅ Current price  
  - ✅ Sector  
✔️ Allow **adjustable filtering settings** from the GUI  
✔️ Apply **CustomTkinter styling**  

⏩ **Responsible Agents:**  
- **Feature Developer AI** → Implements the GUI  
- **Lead Developer AI** → Reviews & merges updates  
- **Code Review AI** → Ensures UI/UX consistency  

---

### **🔹 Phase 4: Optimization & Testing (Week 7-8)**
✔️ Optimize API calls (stay within **120-order limit**)  
✔️ Implement unit tests for:  
  - ✅ **Stock filtering logic**  
  - ✅ **API authentication**  
  - ✅ **Session persistence**  
✔️ Final debugging & performance improvements  

⏩ **Responsible Agents:**  
- **Optimization AI** → Improves speed & efficiency  
- **Automated Testing AI** → Runs performance tests  
- **Code Review AI** → Ensures clean, optimized code  

---

### **🔹 Phase 5: Deployment & Documentation (Week 9)**
✔️ Prepare production-ready branch (`deploy/main`)  
✔️ Final API key security checks  
✔️ **Deployment AI** pushes final version  
✔️ **Documentation AI** updates all documentation  

⏩ **Responsible Agents:**  
- **Deployment AI** → Handles production deployment  
- **Documentation AI** → Finalizes README & API references  

---

## **📌 Security Considerations**
🔹 **OAuth 2.0 Authentication:** Secure login via Charles Schwab API  
🔹 **Token Storage:** Credentials are stored securely using **Keyring**  
🔹 **No Local Database:** Always fetch fresh stock data directly from API  
🔹 **Callback URL:** Set to `https://127.0.0.1` for secure authentication  

---

## **📌 Additional Features (Post-Launch)**
✅ **Export results to CSV**  
✅ **Dark mode UI**  
✅ **Multi-threading for faster API calls**  
✅ **More fundamental data metrics**  

---

## **📌 Repository File Structure**
The project follows a **modular, professional architecture**.

```
stock_scanner/
│── src/
│   ├── main.py                     # Entry point, initializes app & GUI
│   ├── gui/                         # GUI Layer
│   │   ├── app.py                   # Main application window
│   │   ├── sidebar.py               # Sidebar for filters
│   │   ├── results_panel.py         # Scrollable results display
│   ├── api/                         # API Client Layer
│   │   ├── client.py                # Handles API requests
│   │   ├── auth.py                  # Manages authentication
│   │   ├── stock_data.py            # Fetches stock data
│   ├── core/                        # Business Logic
│   │   ├── scanner.py               # Stock filtering logic
│   │   ├── filters.py               # Implements filtering criteria
│── docs/                            # Documentation
│   ├── dev-plan.md                  # Development roadmap
│   ├── API_reference.md             # API integration notes
│── tests/                           # Unit Tests
│── README.md                        # Project overview
│── requirements.txt                 # Dependencies list
```

---

## **📌 Final Notes**
✔️ **Every AI agent has clear tasks**  
✔️ **All documentation is structured**  
✔️ **The development roadmap is optimized for efficiency**  
