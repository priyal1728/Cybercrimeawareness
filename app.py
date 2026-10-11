from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Cybercrime awareness topics
topics = {
    "online-fraud": {
        "title": "Online Fraud",
        "icon": "🔐",
        "description": "Learn to recognize payment scams, fake offers, and online shopping fraud.",
        "intro": "Learn to recognize payment scams, fake offers, and online shopping fraud.",
        "what": "Online fraud happens when scammers trick people into sending money or sharing banking details through fake offers, websites, or payment requests.",
        "details": [
            "Fraudsters often use fake shopping websites, too-good-to-be-true deals, or urgent payment demands to pressure victims.",
            "They may impersonate sellers, delivery services, or even trusted brands to gain trust before asking for payment.",
            "Once money is sent, it is often difficult to recover, especially if the fake account or website disappears quickly.",
            "Victims may lose money, personal information, or access to their accounts when payment details are exposed."
        ],
        "signs": [
            "Offers that seem too good to be true",
            "Requests for payment using unknown personal accounts",
            "Messages claiming you won a prize and must pay a fee first",
            "Transaction alerts that do not match your actual activity"
        ],
        "example": "A fake shopping website advertises a mobile phone at a very low price. After payment, the product never arrives and the seller disappears.",
        "protect": [
            "Shop only on trusted websites.",
            "Verify the seller and website before paying.",
            "Never share your OTP, PIN, or password with anyone.",
            "Check transaction alerts regularly."
        ],
        "prevention": [
            "Verify websites before making payments.",
            "Never share your UPI PIN or OTP.",
            "Avoid offers that seem too good to be true.",
            "Use trusted payment methods."
        ]
    },
    "phishing": {
        "title": "Phishing Awareness",
        "icon": "🎣",
        "description": "Understand how suspicious emails, messages, and links can trick users.",
        "intro": "Understand how suspicious emails, messages, and links can trick users.",
        "what": "Phishing is a scam that pretends to be a bank, delivery company, or trusted service to steal sensitive information using fake messages or websites.",
        "details": [
            "Phishing messages often create urgency, such as telling you your account will be blocked unless you act immediately.",
            "Attackers may use fake domains that look almost identical to real websites, adding small changes in spelling or branding.",
            "Shortened URLs, fake QR codes, and unexpected attachments are common methods used to hide scam websites.",
            "Once the victim enters personal data, the attacker can steal passwords, OTPs, card details, or account access."
        ],
        "signs": [
            "Urgent messages demanding immediate action",
            "Misspellings in a website address",
            "Unknown attachments or shortened links",
            "Requests for passwords, card details, or OTPs"
        ],
        "example": "You receive a message that looks like it came from your bank, asking you to click a link to unblock your account. The link leads to a fake website created to steal your details.",
        "protect": [
            "Verify the sender before clicking any link.",
            "Type the official website directly into the browser.",
            "Do not download unknown attachments.",
            "Do not reply to suspicious messages; verify through official channels."
        ],
        "prevention": [
            "Do not click suspicious links.",
            "Verify the sender before responding.",
            "Never share passwords or OTPs.",
            "Use multi-factor authentication."
        ]
    },
    "identity-theft": {
        "title": "Identity Theft",
        "icon": "🪪",
        "description": "Learn how to protect your personal information and online accounts.",
        "intro": "Learn how to protect your personal information and online accounts.",
        "what": "Identity theft happens when someone misuses another person's personal information, account access, or identity documents without permission.",
        "details": [
            "Criminals may collect personal details from leaked data, social media profiles, fake surveys, or malicious apps.",
            "Once they have enough information, they may open accounts, apply for services, or impersonate the victim online.",
            "This can lead to financial loss, account takeover, reputation damage, and difficulty proving the victim is innocent.",
            "Identity theft often continues unnoticed until the victim sees unexpected transactions or account alerts."
        ],
        "signs": [
            "Accounts or transactions you never created",
            "Password reset messages you did not request",
            "Unexpected login notifications",
            "Messages sent from your account without your knowledge"
        ],
        "example": "Someone obtains your password and logs into your social media account, then sends messages pretending to be you.",
        "protect": [
            "Do not publicly share personal documents or sensitive details.",
            "Use a different strong password for every account.",
            "Enable two-factor authentication.",
            "If you see unknown login activity, change your password and contact support."
        ],
        "prevention": [
            "Keep personal information private.",
            "Use strong and unique passwords.",
            "Avoid sharing sensitive information on public platforms.",
            "Monitor your accounts for suspicious activity."
        ]
    },
    "cyberbullying": {
        "title": "Cyberbullying",
        "icon": "💬",
        "description": "Understand online harassment, blocking, and reporting.",
        "intro": "Understand online harassment, blocking, and reporting.",
        "what": "Cyberbullying includes repeated online insults, threats, humiliation, or harassment directed at a person through social media, games, or messaging apps.",
        "details": [
            "Cyberbullying may happen through messages, social media comments, group chats, gaming platforms, or fake accounts.",
            "The effect can be emotional distress, fear, embarrassment, and loss of confidence for the victim.",
            "In severe cases, it can escalate into threats, blackmail, or coordinated harassment across multiple platforms.",
            "Reporting and documenting incidents early can reduce damage and help adults or authorities take action."
        ],
        "signs": [
            "Repeated insulting or threatening messages",
            "Sharing private photos or information without consent",
            "Being targeted in an online group",
            "Threats or fake profiles created to embarrass someone"
        ],
        "example": "Several people in an online group repeatedly insult one person and share harmful posts about them.",
        "protect": [
            "Save evidence of messages and account activity.",
            "Use block and report tools on the platform.",
            "Talk to a trusted adult, teacher, or guardian.",
            "If threatened or unsafe, seek help from a trusted person or local authority."
        ],
        "prevention": [
            "Block and report abusive accounts.",
            "Save evidence of threatening messages.",
            "Avoid responding to abusive messages.",
            "Tell a trusted adult or appropriate authority."
        ]
    }
}

# Online safety practices
practices = {
    "strong-passwords": {
        "title": "Strong Passwords",
        "description": "Strong passwords help protect your accounts from unauthorized access.",
        "steps": [
            "Use long and unique passwords.",
            "Avoid personal details in passwords.",
            "Do not reuse passwords across accounts.",
            "Use a trusted password manager if appropriate."
        ]
    },
    "two-factor-authentication": {
        "title": "Two-Factor Authentication",
        "description": "Two-factor authentication adds another verification step when signing in.",
        "steps": [
            "Enable two-factor authentication where available.",
            "Use an authenticator app or another supported secure method.",
            "Keep recovery options updated.",
            "Never share verification codes with others."
        ]
    },
    "safe-browsing": {
        "title": "Safe Browsing",
        "description": "Safe browsing helps reduce the risk of scams, malicious downloads, and data theft.",
        "steps": [
            "Check website addresses carefully.",
            "Avoid unknown downloads.",
            "Keep your browser updated.",
            "Do not ignore security warnings."
        ]
    },
    "privacy-protection": {
        "title": "Privacy Protection",
        "description": "Privacy protection helps you control who can access your personal information online.",
        "steps": [
            "Review your social media privacy settings.",
            "Share personal information carefully.",
            "Disable unnecessary app permissions.",
            "Avoid sensitive activities on public Wi-Fi."
        ]
    }
}

# Quiz questions
questions = [
    {
        "question": "What is phishing?",
        "options": [
            "A method of stealing information using deceptive messages",
            "A way to improve internet speed",
            "A computer hardware upgrade",
            "A method of backing up files"
        ],
        "answer": 0,
        "explanation": "Phishing uses deceptive messages or websites to trick people into revealing information."
    },
    {
        "question": "Should you share an OTP with a stranger?",
        "options": [
            "Yes, if they ask politely",
            "Yes, if they claim to be from a bank",
            "No, never share it with an unverified person",
            "Only on social media"
        ],
        "answer": 2,
        "explanation": "Never disclose an OTP to an unverified person, even if they claim to represent a bank."
    },
    {
        "question": "Which password practice is safer?",
        "options": [
            "Using your name and birth year",
            "Using the same password everywhere",
            "Sharing your password with friends",
            "Using a long, unique password for each account"
        ],
        "answer": 3,
        "explanation": "Long, unique passwords reduce the risk of one compromised account affecting other accounts."
    },
    {
        "question": "What should you do if someone cyberbullies you?",
        "options": [
            "Share your password with them",
            "Block and report the account and seek help",
            "Send them your personal information",
            "Click every link they send"
        ],
        "answer": 1,
        "explanation": "Blocking and reporting the account and seeking help are safer responses to cyberbullying."
    },
    {
        "question": "What does two-factor authentication provide?",
        "options": [
            "An additional verification step",
            "Unlimited internet access",
            "Automatic deletion of all malware",
            "Free online shopping"
        ],
        "answer": 0,
        "explanation": "Two-factor authentication adds another verification step to help secure an account."
    },
    {
        "question": "Which action helps protect against malware?",
        "options": [
            "Opening every email attachment",
            "Downloading unknown software",
            "Installing updates and using trusted downloads",
            "Ignoring security warnings"
        ],
        "answer": 2,
        "explanation": "Updates and trusted downloads help reduce exposure to malicious software."
    },
    {
        "question": "What is identity theft?",
        "options": [
            "Improving a computer's performance",
            "Using another person's information without permission",
            "Creating a backup",
            "Changing a website's theme"
        ],
        "answer": 1,
        "explanation": "Identity theft involves unauthorized use of another person's personal information."
    },
    {
        "question": "What should you do before making an online payment?",
        "options": [
            "Share your UPI PIN with the seller",
            "Ignore the payment details",
            "Trust every link in a message",
            "Verify the website and payment request"
        ],
        "answer": 3,
        "explanation": "Verify the website and payment request before sending money."
    }
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        topics=topics,
        practices=practices
    )


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/logout")
def logout():
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/topic/<slug>")
def topic_detail(slug):
    item = topics.get(slug)

    if item is None:
        return render_template(
            "error.html",
            message="The requested cybercrime topic was not found."
        ), 404

    return render_template(
        "detail.html",
        item=item,
        kind="Cybercrime Topic"
    )


@app.route("/practice/<slug>")
def practice_detail(slug):
    item = practices.get(slug)

    if item is None:
        return render_template(
            "error.html",
            message="The requested safety practice was not found."
        ), 404

    return render_template(
        "detail.html",
        item=item,
        kind="Safety Practice"
    )


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    score = None
    results = []

    if request.method == "POST":
        for index, question in enumerate(questions):
            selected = request.form.get(f"q{index}")

            try:
                selected_index = int(selected)
            except (TypeError, ValueError):
                selected_index = -1

            is_correct = selected_index == question["answer"]

            results.append({
                "question": question["question"],
                "selected": selected_index,
                "correct": question["answer"],
                "is_correct": is_correct,
                "explanation": question["explanation"],
                "options": question["options"]
            })

        score = sum(
            1 for result in results if result["is_correct"]
        )

    return render_template(
        "quiz.html",
        questions=questions,
        score=score,
        results=results
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "error.html",
        message="The page you requested could not be found."
    ), 404


if __name__ == "__main__":
    app.run(debug=True)