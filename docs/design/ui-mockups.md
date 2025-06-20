# Hirova AI - UI Mockups & Design Specifications

## Design System Overview

### Brand Colors
```css
--primary: #4F46E5 (Indigo-600)
--primary-dark: #4338CA (Indigo-700)
--secondary: #10B981 (Emerald-500)
--accent: #F59E0B (Amber-500)
--danger: #EF4444 (Red-500)
--background: #F9FAFB (Gray-50)
--surface: #FFFFFF
--text-primary: #111827 (Gray-900)
--text-secondary: #6B7280 (Gray-500)
```

### Typography
- **Headers**: Inter (Bold)
- **Body**: Inter (Regular)
- **Monospace**: JetBrains Mono

## 1. Landing Page

```
┌─────────────────────────────────────────────────────────────────┐
│ [Hirova AI Logo]                    Home  Features  Pricing  Login│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│      ┌─────────────────────────────────────────────────┐      │
│      │                                                   │      │
│      │   Find Your Perfect Candidate in Seconds         │      │
│      │                                                   │      │
│      │   AI-powered recruitment that reduces            │      │
│      │   time-to-hire by 70% while eliminating bias     │      │
│      │                                                   │      │
│      │   [Start Free Trial]  [Watch Demo]               │      │
│      │                                                   │      │
│      └─────────────────────────────────────────────────┘      │
│                                                                 │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐   │
│  │ 📊          │ 🎯          │ ⚡          │ 🔒          │   │
│  │ 70% Faster  │ 94% Match   │ Real-time   │ Enterprise  │   │
│  │ Hiring      │ Accuracy     │ Screening   │ Security    │   │
│  └─────────────┴─────────────┴─────────────┴─────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 2. Dashboard (Main View)

```
┌─────────────────────────────────────────────────────────────────┐
│ Hirova AI  [🔍 Search]                    [🔔] [Jane D.] [⚙️]   │
├─────┬───────────────────────────────────────────────────────────┤
│     │                                                           │
│ 📊  │  Welcome back, Jane!                                     │
│     │                                                           │
│ 🏢  │  ┌─────────────┬─────────────┬─────────────┬──────────┐ │
│     │  │ Active Jobs │ Candidates  │ Interviews  │ Offers   │ │
│ 👥  │  │     12      │     156     │     23      │    5     │ │
│     │  └─────────────┴─────────────┴─────────────┴──────────┘ │
│ 📈  │                                                           │
│     │  Recent Activity                                          │
│ 💬  │  ┌───────────────────────────────────────────────────┐   │
│     │  │ • John Doe completed AI screening - 92% match     │   │
│ ⚙️  │  │ • 5 new applications for Senior Developer        │   │
│     │  │ • Interview scheduled: Sarah Chen - 2:00 PM      │   │
│     │  │ • AI Assistant sent 12 follow-up emails          │   │
│     │  └───────────────────────────────────────────────────┘   │
│     │                                                           │
│     │  Top Candidates This Week                                │
│     │  ┌─────────────────────────────────────────────────┐     │
│     │  │ [Photo] John Doe      | Senior Dev   | 92% |⭐│     │
│     │  │ [Photo] Sarah Chen    | Product Mgr  | 89% |⭐│     │
│     │  │ [Photo] Mike Wilson   | Designer     | 87% |⭐│     │
│     │  └─────────────────────────────────────────────────┘     │
└─────┴───────────────────────────────────────────────────────────┘
```

## 3. Job Posting Creation

```
┌─────────────────────────────────────────────────────────────────┐
│ ← Back to Jobs                                      [Save Draft]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Create New Job Posting                                         │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Job Title *                                              │   │
│  │ [Senior Frontend Developer                            ]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────┬───────────────────────────────────┐   │
│  │ Department          │ Location                           │   │
│  │ [Engineering    ▼]  │ [San Francisco, CA            ]   │   │
│  └─────────────────────┴───────────────────────────────────┘   │
│                                                                 │
│  Application Methods (Select all that apply)                   │
│  ☑ LinkedIn Quick Apply (Recommended)                          │
│  ☑ Email Applications to: apply@company.hirova.ai             │
│  ☑ Indeed Integration                                          │
│  ☑ Direct Upload                                               │
│  ☑ Resume Builder                                              │
│  ☐ Application Form Only (Not Recommended)                     │
│                                                                 │
│  💡 Tip: Enabling multiple methods increases applications by 3x │
│                                                                 │
│  Job Description                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ We are looking for a talented Frontend Developer to     │   │
│  │ join our team...                                         │   │
│  │                                                          │   │
│  │ [AI Enhance 🤖] - Let AI improve your job description   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Required Skills (AI will match these)                         │
│  [React] [TypeScript] [+Add Skill]                            │
│                                                                 │
│  Nice-to-Have Skills                                           │
│  [Next.js] [GraphQL] [+Add Skill]                             │
│                                                                 │
│         [Cancel]  [Save as Draft]  [Publish & Start Screening] │
└─────────────────────────────────────────────────────────────────┘
```

Note: The original job posting creation screen has been updated to include application method selection, emphasizing the multiple ways candidates can apply.

## 3a. Original Job Posting Creation (Continued)

```
┌─────────────────────────────────────────────────────────────────┐
│ ← Back to Jobs                                      [Save Draft]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Create New Job Posting                                         │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Job Title *                                              │   │
│  │ [Senior Frontend Developer                            ]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────┬───────────────────────────────────┐   │
│  │ Department          │ Location                           │   │
│  │ [Engineering    ▼]  │ [San Francisco, CA            ]   │   │
│  └─────────────────────┴───────────────────────────────────┘   │
│                                                                 │
│  Job Description                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ We are looking for a talented Frontend Developer to     │   │
│  │ join our team...                                         │   │
│  │                                                          │   │
│  │ [AI Enhance 🤖] - Let AI improve your job description   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Required Skills (AI will match these)                         │
│  [React] [TypeScript] [+Add Skill]                            │
│                                                                 │
│  Nice-to-Have Skills                                           │
│  [Next.js] [GraphQL] [+Add Skill]                             │
│                                                                 │
│         [Cancel]  [Save as Draft]  [Publish & Start Screening] │
└─────────────────────────────────────────────────────────────────┘
```

## 4. Candidate List View

```
┌─────────────────────────────────────────────────────────────────┐
│ Candidates for: Senior Frontend Developer          [Export CSV] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ [🔍 Search candidates]  [Filter ▼]  [Sort: Match Score ▼]      │
│                                                                 │
│ Showing 1-10 of 156 candidates                                 │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ □ | Photo | Name          | Match | Status    | Actions    │ │
│ ├─────────────────────────────────────────────────────────────┤ │
│ │ □ | [👤]  | John Doe      | 92%   | Screened  | [View][✉️] │ │
│ │   |       | 5 yrs React, TypeScript expert                  │ │
│ ├─────────────────────────────────────────────────────────────┤ │
│ │ □ | [👤]  | Sarah Chen    | 89%   | New       | [View][✉️] │ │
│ │   |       | 4 yrs Frontend, Next.js specialist              │ │
│ ├─────────────────────────────────────────────────────────────┤ │
│ │ □ | [👤]  | Mike Wilson   | 87%   | Interview | [View][✉️] │ │
│ │   |       | 6 yrs experience, Full-stack background         │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ [Previous] Page 1 of 16 [Next]                                 │
│                                                                 │
│ Bulk Actions: [Send Email] [Schedule Interview] [Export]       │
└─────────────────────────────────────────────────────────────────┘
```

## 5. Candidate Detail View

```
┌─────────────────────────────────────────────────────────────────┐
│ ← Back to Candidates                    [Schedule Interview] [✉️]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ ┌───────────┬───────────────────────────────────────────────┐   │
│ │   [👤]    │ John Doe                          92% Match   │   │
│ │           │ Senior Frontend Developer                     │   │
│ │           │ 📧 john.doe@email.com  📱 (555) 123-4567     │   │
│ │           │ 📍 San Francisco, CA                          │   │
│ └───────────┴───────────────────────────────────────────────┘   │
│                                                                 │
│ [Overview] [AI Analysis] [Resume] [Notes] [Activity]           │
│ ─────────────────────────────────────────────────────────────   │
│                                                                 │
│ AI Analysis Summary                                             │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ ✅ Strong Match - Recommended for Interview               │     │
│ │                                                          │     │
│ │ Key Strengths:                                           │     │
│ │ • 5 years React experience (Required: 3+)               │     │
│ │ • Expert in TypeScript and modern JS                    │     │
│ │ • Led team of 3 developers at previous role             │     │
│ │                                                          │     │
│ │ Potential Concerns:                                      │     │
│ │ • No direct Next.js experience (nice-to-have)           │     │
│ │ • Salary expectations may be above range                │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ AI Screening Conversation                      [View Full Chat] │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ AI: Tell me about your React experience.                │     │
│ │ JD: I've been working with React for 5 years...         │     │
│ └─────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

## 6. Application Methods Screen (Candidate View)

```
┌─────────────────────────────────────────────────────────────────┐
│              Apply for Senior Frontend Developer                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Choose how you'd like to share your experience:               │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [LinkedIn Logo] Import from LinkedIn          [Connect] │   │
│  │ ⭐ Recommended - One click, no manual entry             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [Indeed Logo] Apply with Indeed Profile      [Connect]  │   │
│  │ Use your existing Indeed resume                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ✉️ Email Your Resume                                     │   │
│  │ Send to: apply-7x9k2@techco.hirova.ai                  │   │
│  │                                        [Copy Address]   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 📄 Paste Resume Text                    [Start Typing]  │   │
│  │ No file? Just paste your resume content               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 📎 Upload Resume File                   [Choose File]   │   │
│  │ PDF, DOCX, or TXT (Max 10MB)                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🔨 Build Your Resume                    [Start Builder] │   │
│  │ Use our AI-powered resume builder                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ───────────────── For Recruiters Only ─────────────────────    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🤖 AI Talent Scout                    [Setup]          │   │
│  │ Let AI search your resume database for matches        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## 7. AI Screening Chat Interface (After Resume Submission)

```
┌─────────────────────────────────────────────────────────────────┐
│                     Hirova AI Screening                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Great! I've received your information. Now let's have a       │
│  quick conversation about your experience.                     │
│                                                                 │
│  This will take about 10-15 minutes. Ready to start?          │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │                                                             │ │
│ │  AI: Thanks for applying! Let's start with your            │ │
│ │      experience. Can you tell me about your most           │ │
│ │      recent React project?                                 │ │
│ │                                                             │ │
│ │  You: Sure! I recently led the development of a            │ │
│ │       large-scale e-commerce platform using React...       │ │
│ │                                                             │ │
│ │  AI: That sounds impressive! What were the main            │ │
│ │      technical challenges you faced?                       │ │
│ │                                                             │ │
│ │  You: The biggest challenge was implementing real-time     │ │
│ │       inventory updates across thousands of products...    │ │
│ │                                                             │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ [Type your response...]                                   [Send] │
│                                                                 │
│ Progress: ████████░░ 80% Complete                              │
└─────────────────────────────────────────────────────────────────┘
```

## 7. Analytics Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│ Analytics Overview                    [Last 30 Days ▼] [Export] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ ┌────────────────┬────────────────┬────────────────┬─────────┐ │
│ │ Time to Hire   │ Cost per Hire  │ Quality Score  │ Diversity│ │
│ │ 14 days        │ $847           │ 8.7/10         │ 68%     │ │
│ │ ↓ 35%          │ ↓ 42%          │ ↑ 12%          │ ↑ 5%    │ │
│ └────────────────┴────────────────┴────────────────┴─────────┘ │
│                                                                 │
│ Hiring Funnel                                                   │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Applied        ████████████████████████ 523             │     │
│ │ AI Screened    ███████████████ 342                      │     │
│ │ Interviewed    ██████ 89                                 │     │
│ │ Offered        ██ 23                                     │     │
│ │ Hired          █ 18                                      │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ Source Effectiveness                                            │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ LinkedIn       ████████████ 45%                         │     │
│ │ Indeed         ████████ 30%                             │     │
│ │ Company Site   ████ 15%                                 │     │
│ │ Referrals      ██ 10%                                   │     │
│ └─────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

## 8. Mobile App Views

### Mobile Dashboard
```
┌─────────────────┐
│ 📱 Hirova AI    │
│ ≡  Dashboard  🔔│
├─────────────────┤
│                 │
│ Active Jobs: 12 │
│ New Today: 23   │
│                 │
│ ┌─────────────┐ │
│ │ Recent      │ │
│ │             │ │
│ │ • John Doe  │ │
│ │   92% match │ │
│ │   [View]    │ │
│ │             │ │
│ │ • Sarah C.  │ │
│ │   89% match │ │
│ │   [View]    │ │
│ └─────────────┘ │
│                 │
│ [+] Post Job    │
└─────────────────┘
```

### Mobile Candidate View
```
┌─────────────────┐
│ 📱 < Candidates │
├─────────────────┤
│ [👤]            │
│ John Doe        │
│ 92% Match       │
│                 │
│ ┌─────────────┐ │
│ │ AI Summary  │ │
│ │             │ │
│ │ ✅ Strong   │ │
│ │ candidate   │ │
│ │             │ │
│ │ • 5y React  │ │
│ │ • Team lead │ │
│ └─────────────┘ │
│                 │
│ [📧 Contact]    │
│ [📅 Schedule]   │
│                 │
│ [View Resume]   │
└─────────────────┘
```

## 9. AI Interview Coach Screen

```
┌─────────────────────────────────────────────────────────────────┐
│ AI Interview Coach - Practice for: Senior Developer    [Exit]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    [🎥 Video Window]                    │   │
│  │                                                          │   │
│  │                    Your Video Feed                       │   │
│  │                                                          │   │
│  │              AI Coach: "Tell me about                    │   │
│  │              your React experience"                      │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ⏱️ 00:45 / 02:00              [⏸️ Pause] [🔴 End Answer]       │
│                                                                 │
│  Real-time Feedback:                                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ✅ Good eye contact                                     │   │
│  │ ✅ Clear speech pace                                    │   │
│  │ ⚠️ Try to smile more - you seem nervous                │   │
│  │ 💡 Mention specific project examples                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Overall Performance:                                           │
│  Confidence: ███████░░░ 70%                                     │
│  Content:    ████████░░ 80%                                     │
│  Body Lang:  ██████░░░░ 60%                                     │
│                                                                 │
│  [View Report] [Try Again] [Next Question]                     │
└─────────────────────────────────────────────────────────────────┘
```

## 10. Skills Gap Analyzer

```
┌─────────────────────────────────────────────────────────────────┐
│ Skills Gap Analysis for: Senior Frontend Developer             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Your Current Match: 72%                                         │
│                                                                 │
│ ✅ Skills You Have:                                             │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ • React (5 years) - Required ✓                          │     │
│ │ • JavaScript (7 years) - Required ✓                     │     │
│ │ • CSS/HTML (8 years) - Required ✓                      │     │
│ │ • Git (5 years) - Required ✓                           │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ 🎯 Skills to Learn:                                            │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ TypeScript (Required)                    🔴 Critical    │     │
│ │ Time to Learn: 2-3 weeks                                 │     │
│ │ [🎓 Free Course] [📚 Documentation] [🎮 Practice]      │     │
│ ├─────────────────────────────────────────────────────────┤     │
│ │ Next.js (Nice to have)                   🟡 Medium     │     │
│ │ Time to Learn: 1-2 weeks                                 │     │
│ │ [🎓 Free Course] [📚 Documentation] [🎮 Practice]      │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ 💡 Alternative Paths:                                          │
│ • React Developer at TechCo - 95% match (Apply Now)           │
│ • Frontend Engineer at StartupX - 88% match                   │
│ • UI Developer at CorpY - 91% match                           │
│                                                                 │
│ [Create Learning Plan] [Find Similar Jobs] [Get Mentorship]    │
└─────────────────────────────────────────────────────────────────┘
```

## 11. Team Chemistry & Predictive Analytics Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│ Predictive Hiring Intelligence - John Doe              [Back]   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ 🔮 AI Predictions:                                             │
│                                                                 │
│ ┌───────────────────┬───────────────────┬───────────────────┐ │
│ │ 2-Year Retention  │ Performance       │ Promotion Ready   │ │
│ │ 87% 🟢            │ 4.2/5.0 🔵        │ 14 months 🟡      │ │
│ │ Industry Avg: 72% │ Team Avg: 3.8     │ Avg: 18 months    │ │
│ └───────────────────┴───────────────────┴───────────────────┘ │
│                                                                 │
│ 🤝 Team Chemistry Analysis:                                    │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Current Team Composition:                                │     │
│ │                                                          │     │
│ │   [Sarah]  [Mike]  [Emma]  [+John]  [Team]              │     │
│ │     INTJ    ENFP    ISTP    ENTP                        │     │
│ │                                                          │     │
│ │ Team Balance Score: 92/100 🎆                            │     │
│ │                                                          │     │
│ │ ✅ Complementary thinking styles                        │     │
│ │ ✅ Good introvert/extrovert balance                    │     │
│ │ ✅ John's style complements Sarah well                  │     │
│ │ ⚠️ Potential conflict with Mike (coach manager)        │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ 📈 Success Factors:                                            │
│ • Strong technical background matches team needs              │
│ • Previous startup experience aligns with culture             │
│ • Communication style fits remote-first environment           │
│                                                                 │
│ [Full Report] [Compare Candidates] [Schedule with Team]        │
└─────────────────────────────────────────────────────────────────┘
```

## 12. Career Path Visualizer

```
┌─────────────────────────────────────────────────────────────────┐
│ Your Career Journey from: Senior Frontend Developer    [💾 Save]│
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  NOW          1-2 YRS        3-5 YRS        5-10 YRS          │
│   │             │              │              │               │
│   ●─────────────►──────────────►──────────────►              │
│   │             │              │              │               │
│ [👨‍💻]        [👨‍💼]          [👨‍🏫]          [🏆]             │
│ Sr Frontend   Tech Lead      Architect      CTO/VP Eng        │
│ $120-150k     $150-180k      $180-220k      $250k+           │
│                                                                 │
│                  └──────────────► Engineering Manager        │
│                              $160-200k                         │
│                                 │                              │
│                  └──────────────► Product Engineer          │
│                              $140-170k                         │
│                                                                 │
│ Skills You'll Gain:                                            │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Year 1: System Design, Team Leadership, Architecture    │     │
│ │ Year 2: Business Strategy, Public Speaking, Mentoring   │     │
│ │ Year 3-5: Executive Presence, P&L Management           │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ Success Stories from This Company:                             │
│ • Sarah Chen: Frontend → Tech Lead → VP Eng (4 years)        │
│ • Mike Rodriguez: Frontend → Architect (3 years)             │
│                                                                 │
│ [View Detailed Roadmap] [Connect with Mentors] [Set Goals]    │
└─────────────────────────────────────────────────────────────────┘
```

## 13. AI Reference Check Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│ Automated Reference Check - John Doe                  [Export] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Reference Check Status: 2/3 Complete                           │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Reference 1: Sarah Martinez (Former Manager)            │     │
│ │ Status: ✅ Complete | Response Time: 18 hours           │     │
│ │                                                          │     │
│ │ Overall Rating: ⭐⭐⭐⭐⭐ (5/5)                          │     │
│ │ Would Rehire: Yes, immediately                           │     │
│ │                                                          │     │
│ │ Key Insights:                                            │     │
│ │ • "Top 5% of developers I've worked with"               │     │
│ │ • Strong technical skills, excellent communicator        │     │
│ │ • Only weakness: Sometimes too perfectionist            │     │
│ │                                                          │     │
│ │ Sentiment Analysis: 92% Positive 🟢                      │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Reference 2: Mike Chen (Peer)                           │     │
│ │ Status: ✅ Complete | Response Time: 6 hours            │     │
│ │                                                          │     │
│ │ Overall Rating: ⭐⭐⭐⭐ (4/5)                            │     │
│ │ Team Player Score: 9/10                                  │     │
│ │                                                          │     │
│ │ Key Insights:                                            │     │
│ │ • Great collaborator, always willing to help            │     │
│ │ • Innovative problem solver                              │     │
│ │ • Could delegate more instead of doing everything       │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Reference 3: Lisa Park (Direct Report)                  │     │
│ │ Status: ⏳ Pending | Sent: 2 days ago | [Resend]       │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ AI Summary: Strong candidate with consistent positive feedback │
│                                                                 │
│ [View Full Responses] [Request Additional] [Share with Team]   │
└─────────────────────────────────────────────────────────────────┘
```

## 14. AI Talent Scout Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│ AI Talent Scout - Continuous Candidate Discovery    [Settings] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ 🤖 Status: Active | Last Scan: 2 minutes ago | Next: 58 min   │
│                                                                 │
│ Monitored Sources:                                              │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ ✓ Local: /resumes/2024/        | 3,847 files | Daily   │     │
│ │ ✓ Google Drive: HR Folder      | 1,234 files | Hourly  │     │
│ │ ✓ Email: resumes@company.com   | 567 emails  | Real-time│     │
│ │ + Add Source                                             │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ Recent AI Discoveries:                                          │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ 🎯 Found 12 new matches in last 24 hours                │     │
│ │                                                          │     │
│ │ • Emma Thompson - 94% match for Senior Developer        │     │
│ │   Source: Google Drive | Found: 10 min ago              │     │
│ │   [Review] [Contact] [Add to Pipeline]                  │     │
│ │                                                          │     │
│ │ • David Kim - 91% match for Product Manager            │     │
│ │   Source: 2023 Archive | Found: 2 hours ago            │     │
│ │   [Review] [Contact] [Add to Pipeline]                  │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ AI Matching Rules:                                             │
│ ┌─────────────────────────────────────────────────────────┐     │
│ │ Active Jobs: 8 positions                                 │     │
│ │ Min Match Score: 85%                                     │     │
│ │ Experience Range: 2-10 years                             │     │
│ │ Location: Remote or San Francisco                        │     │
│ │                                    [Edit Rules]          │     │
│ └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│ Performance:                                                    │
│ Total Scanned: 45,892 | Matches Found: 234 | Hired: 18        │
└─────────────────────────────────────────────────────────────────┘
```

## Design Components Library

### Buttons
```
Primary:   [━━━━━━━━━━] (Indigo-600, White text)
Secondary: [┅┅┅┅┅┅┅┅┅┅] (White, Indigo border)
Success:   [━━━━━━━━━━] (Emerald-500, White text)
Danger:    [━━━━━━━━━━] (Red-500, White text)
```

### Cards
```
┌─────────────────────┐
│ Card Header         │
├─────────────────────┤
│ Card content goes   │
│ here with proper    │
│ padding and spacing │
└─────────────────────┘
```

### Form Elements
```
Text Input:
┌─────────────────────┐
│ Placeholder text    │
└─────────────────────┘

Select Dropdown:
┌─────────────────▼───┐
│ Select option       │
└─────────────────────┘

Checkbox:
☐ Option label
☑ Selected option
```

### Status Badges
```
[● New]      (Gray)
[● Screening] (Blue)
[● Interview] (Yellow)
[● Offered]   (Green)
[● Rejected]  (Red)
```

## Responsive Breakpoints

- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

## Accessibility Requirements

- WCAG 2.1 AA compliance
- Keyboard navigation support
- Screen reader compatibility
- High contrast mode
- Minimum touch target: 44x44px
- Color contrast ratio: 4.5:1 minimum

## Animation Guidelines

- Use subtle transitions (200-300ms)
- Ease-in-out timing function
- Loading states with skeletons
- Micro-interactions on hover/click
- Progress indicators for long operations

---

*These mockups serve as a visual guide for development. Final implementation may vary based on user testing and technical constraints.*