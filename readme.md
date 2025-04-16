# Event Manager API : Srikar 

A FastAPI-based system with user authentication, email verification, and secure login, following modern best practices in asynchronous web development. This project uses OAuth2, Pydantic validation, Docker, and GitHub Actions for security and deployment.

---

## ✅ Closed Issues and Fixes

This repository documents five tracked and resolved issues, each with corresponding application code updates and tests:

1. **[#9 - Verification Token Not Being Sent in Email](https://github.com/srikargoud2002/event_manager/issues/9)**  
   Issue involved missing token in the verification email sent to new users. Fixed by injecting `verification_token` in the template context. Now Manual verification also possible.

   ![image](https://github.com/user-attachments/assets/5c9dadd9-836b-48ee-8250-aa46a4d24cd8)


2. **[#7 - Login Page Fix](https://github.com/srikargoud2002/event_manager/issues/7)**  
   Resolved a frontend/backend mismatch that prevented successful login, due to incorrect form handling, made the change to take user input of email instead of username. and also the **example which is said in the video is fixed here now both show the same for easier testing(Registration and LogiN)**.
   
   ![image](https://github.com/user-attachments/assets/402dc37d-5816-42aa-9486-531963464ce1)


3. **[#5 - Password Strength Setting](https://github.com/srikargoud2002/event_manager/issues/5)**  
   Implemented backend validation for password complexity to ensure strong security practices during registration.

   ![image](https://github.com/user-attachments/assets/6aa90141-9e7c-4a2e-b13a-9117e2c084ed)


   

4. **[#3 - Email Validation](https://github.com/srikargoud2002/event_manager/issues/3)**  
   Added Pydantic validation for email field, ensuring proper format and unique constraints before user creation.

   ![image](https://github.com/user-attachments/assets/ef43d60b-5369-4b51-9c33-94eebe8216da)


6. **[#1 - Mismatched Data in Login and Register](https://github.com/srikargoud2002/event_manager/issues/1)**  
   The NickName Issue is fixed here. The Nickname is generated even though there it is being given in the user input. Validation also added to stop duplicates.

All fixes were tested and merged into the `main` branch using GitHub’s pull request workflow.

---

## ALL FILES PASSED THE PYTEST

![image](https://github.com/user-attachments/assets/2f44d863-6312-4639-8996-7e5a296cb86e)

![image](https://github.com/user-attachments/assets/27196609-23bd-41e9-a971-2f7a2aa27b66)


## 🐳 Docker Image

👉 **[DockerHub Image - events-api](https://hub.docker.com/repository/docker/srikar2020/events-api/tags)**  
This public image hosts the latest build of the FastAPI-based Event Manager application. Use it to pull and run the application in any Docker-compatible environment.

---




## 📚 Reflection

This project helped me connect theory with real-world API development. I learned a lot about FastAPI, async database handling, and Pydantic validation. Debugging user issues and setting up CI/CD with Docker and GitHub Actions gave me hands-on experience with secure, maintainable deployments. These skills will be valuable for future team projects and industry work.

---


