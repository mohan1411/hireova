# Hirova AI - API Documentation

## Overview

The Hirova AI API provides programmatic access to our AI-powered recruitment platform. This RESTful API allows you to integrate Hirova's capabilities into your existing systems.

### Base URL
```
Production: https://api.hirova.ai/v1
Staging: https://staging-api.hirova.ai/v1
```

### Authentication

All API requests require authentication using an API key in the header:

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.hirova.ai/v1/jobs
```

## Rate Limits

| Plan | Requests/Hour | Burst |
|------|--------------|-------|
| Free | 100 | 10/min |
| Professional | 1,000 | 100/min |
| Business | 5,000 | 500/min |
| Enterprise | Unlimited | Custom |

## Response Format

All responses follow this structure:

```json
{
  "data": {},
  "meta": {
    "request_id": "req_abc123",
    "timestamp": "2024-01-15T10:30:00Z",
    "version": "1.0"
  },
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 156,
    "pages": 8
  }
}
```

Error responses:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Invalid input provided",
    "details": {
      "field": "email",
      "issue": "Invalid email format"
    }
  },
  "meta": {
    "request_id": "req_abc123",
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## Endpoints

### Authentication

#### POST /auth/token
Exchange credentials for an access token.

**Request:**
```json
{
  "api_key": "YOUR_API_KEY",
  "api_secret": "YOUR_API_SECRET"
}
```

**Response:**
```json
{
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "Bearer",
    "expires_in": 3600
  }
}
```

### Jobs

#### GET /jobs
List all active jobs.

**Query Parameters:**
- `page` (integer): Page number (default: 1)
- `per_page` (integer): Items per page (default: 20, max: 100)
- `status` (string): Filter by status (active, paused, archived)
- `department` (string): Filter by department

**Response:**
```json
{
  "data": [
    {
      "id": "job_123",
      "title": "Senior Frontend Developer",
      "department": "Engineering",
      "location": "San Francisco, CA",
      "status": "active",
      "created_at": "2024-01-10T08:00:00Z",
      "applications_count": 45,
      "matches_count": 12
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 12
  }
}
```

#### POST /jobs
Create a new job posting.

**Request:**
```json
{
  "title": "Senior Frontend Developer",
  "department": "Engineering",
  "location": "San Francisco, CA",
  "description": "We are looking for...",
  "requirements": {
    "required_skills": ["React", "TypeScript", "CSS"],
    "nice_to_have_skills": ["Next.js", "GraphQL"],
    "experience_years": {
      "min": 3,
      "max": 10
    },
    "education": "Bachelor's degree preferred"
  },
  "salary_range": {
    "min": 120000,
    "max": 180000,
    "currency": "USD"
  },
  "remote_policy": "hybrid"
}
```

**Response:**
```json
{
  "data": {
    "id": "job_456",
    "title": "Senior Frontend Developer",
    "status": "active",
    "public_url": "https://careers.company.com/jobs/job_456",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```

#### GET /jobs/{job_id}
Get detailed information about a specific job.

**Response:**
```json
{
  "data": {
    "id": "job_123",
    "title": "Senior Frontend Developer",
    "department": "Engineering",
    "location": "San Francisco, CA",
    "description": "Full job description...",
    "requirements": {
      "required_skills": ["React", "TypeScript"],
      "nice_to_have_skills": ["Next.js"],
      "experience_years": {
        "min": 3,
        "max": 10
      }
    },
    "statistics": {
      "total_applications": 156,
      "screened": 89,
      "interviewed": 12,
      "offers_made": 2
    }
  }
}
```

#### PUT /jobs/{job_id}
Update a job posting.

#### DELETE /jobs/{job_id}
Archive a job posting.

### Candidates

#### GET /jobs/{job_id}/candidates
List candidates for a specific job.

**Query Parameters:**
- `page` (integer): Page number
- `per_page` (integer): Items per page
- `status` (string): Filter by status (new, screened, interviewed, offered, rejected)
- `min_match_score` (integer): Minimum match percentage (0-100)
- `sort` (string): Sort by (match_score, applied_at, name)

**Response:**
```json
{
  "data": [
    {
      "id": "cand_789",
      "name": "John Doe",
      "email": "john.doe@email.com",
      "phone": "+1-555-123-4567",
      "location": "San Francisco, CA",
      "applied_at": "2024-01-14T15:30:00Z",
      "status": "screened",
      "match_score": 92,
      "ai_summary": "Strong candidate with 5 years React experience..."
    }
  ]
}
```

#### GET /candidates/{candidate_id}
Get detailed candidate information.

**Response:**
```json
{
  "data": {
    "id": "cand_789",
    "name": "John Doe",
    "email": "john.doe@email.com",
    "phone": "+1-555-123-4567",
    "location": "San Francisco, CA",
    "resume_url": "https://storage.hirova.ai/resumes/cand_789.pdf",
    "linkedin_url": "https://linkedin.com/in/johndoe",
    "applications": [
      {
        "job_id": "job_123",
        "applied_at": "2024-01-14T15:30:00Z",
        "status": "screened",
        "match_score": 92
      }
    ],
    "skills": ["React", "TypeScript", "Node.js"],
    "experience": {
      "total_years": 5,
      "positions": [
        {
          "title": "Frontend Developer",
          "company": "Tech Corp",
          "duration": "2 years"
        }
      ]
    },
    "education": [
      {
        "degree": "BS Computer Science",
        "institution": "UC Berkeley",
        "year": 2018
      }
    ]
  }
}
```

#### POST /candidates/{candidate_id}/message
Send a message to a candidate.

**Request:**
```json
{
  "subject": "Interview Invitation",
  "body": "Hi John, we'd like to invite you...",
  "template_id": "interview_invite",
  "schedule_at": "2024-01-16T09:00:00Z"
}
```

### Screening

#### POST /screening/start
Initiate AI screening for a candidate.

**Request:**
```json
{
  "candidate_id": "cand_789",
  "job_id": "job_123",
  "questions": [
    "Tell me about your React experience",
    "Describe a challenging project you've worked on"
  ],
  "webhook_url": "https://yourapp.com/webhooks/screening"
}
```

**Response:**
```json
{
  "data": {
    "screening_id": "scr_101",
    "status": "in_progress",
    "estimated_completion": "2024-01-15T11:00:00Z",
    "screening_url": "https://app.hirova.ai/screening/scr_101"
  }
}
```

#### GET /screening/{screening_id}
Get screening results.

**Response:**
```json
{
  "data": {
    "screening_id": "scr_101",
    "candidate_id": "cand_789",
    "job_id": "job_123",
    "status": "completed",
    "completed_at": "2024-01-15T10:45:00Z",
    "match_score": 92,
    "conversation": [
      {
        "role": "ai",
        "content": "Tell me about your React experience",
        "timestamp": "2024-01-15T10:30:00Z"
      },
      {
        "role": "candidate",
        "content": "I have 5 years of experience with React...",
        "timestamp": "2024-01-15T10:31:00Z"
      }
    ],
    "analysis": {
      "strengths": [
        "Strong React expertise",
        "Leadership experience",
        "Clear communication"
      ],
      "concerns": [
        "Limited Next.js experience",
        "Above budget expectations"
      ],
      "recommendation": "STRONG_YES"
    }
  }
}
```

### AI Features

#### POST /ai/interview-coach/start
Start an AI interview coaching session.

**Request:**
```json
{
  "job_id": "job_123",
  "question_type": "behavioral",
  "industry": "tech",
  "difficulty": "senior"
}
```

**Response:**
```json
{
  "data": {
    "session_id": "coach_789",
    "question": "Tell me about a time you led a difficult project",
    "recording_url": "wss://api.hirova.ai/coach/record/coach_789",
    "tips": [
      "Use the STAR method",
      "Quantify your results",
      "Show leadership skills"
    ]
  }
}
```

#### POST /ai/skills-gap/analyze
Analyze skills gap for a candidate.

**Request:**
```json
{
  "candidate_id": "cand_789",
  "job_id": "job_123"
}
```

**Response:**
```json
{
  "data": {
    "match_percentage": 72,
    "has_skills": [
      {
        "skill": "React",
        "years": 5,
        "requirement": "required"
      }
    ],
    "missing_skills": [
      {
        "skill": "TypeScript",
        "requirement": "required",
        "importance": "critical",
        "learning_time": "2-3 weeks",
        "resources": [
          {
            "type": "course",
            "name": "TypeScript Fundamentals",
            "url": "https://...",
            "free": true
          }
        ]
      }
    ],
    "alternative_jobs": [
      {
        "job_id": "job_456",
        "title": "React Developer",
        "match_percentage": 95
      }
    ]
  }
}
```

#### GET /ai/predictive-analytics/{candidate_id}
Get predictive success analytics for a candidate.

**Response:**
```json
{
  "data": {
    "predictions": {
      "retention_2_year": {
        "probability": 0.87,
        "confidence": 0.92,
        "factors": [
          "Strong skill match",
          "Cultural alignment",
          "Growth opportunity fit"
        ]
      },
      "performance_score": {
        "predicted": 4.2,
        "scale": 5,
        "team_average": 3.8
      },
      "promotion_timeline": {
        "months": 14,
        "role": "Senior Developer",
        "confidence": 0.78
      }
    },
    "team_chemistry": {
      "overall_score": 92,
      "personality_fit": "complementary",
      "work_style_match": "high",
      "potential_conflicts": [
        {
          "team_member": "Mike Chen",
          "area": "decision_making_style",
          "severity": "low",
          "mitigation": "Regular 1-on-1s recommended"
        }
      ]
    }
  }
}
```

#### POST /ai/video-analysis
Analyze a video resume.

**Request:**
```json
{
  "video_url": "https://storage.hirova.ai/videos/vid_123.mp4",
  "candidate_id": "cand_789",
  "analysis_type": ["transcription", "soft_skills", "keywords"]
}
```

**Response:**
```json
{
  "data": {
    "analysis_id": "ana_456",
    "transcription": "Full text of video...",
    "soft_skills": {
      "communication": 8.5,
      "confidence": 7.2,
      "enthusiasm": 9.1,
      "professionalism": 8.8
    },
    "keywords_found": ["React", "team leadership", "agile"],
    "highlight_moments": [
      {
        "timestamp": "00:45",
        "description": "Strong example of problem-solving"
      }
    ],
    "overall_impression": "positive",
    "recommendations": "Strong candidate for technical roles"
  }
}
```

### Analytics

#### GET /analytics/overview
Get hiring analytics overview.

**Query Parameters:**
- `start_date` (date): Start of date range
- `end_date` (date): End of date range
- `job_id` (string): Filter by specific job

**Response:**
```json
{
  "data": {
    "metrics": {
      "total_applications": 523,
      "total_hires": 18,
      "average_time_to_hire": 14.5,
      "average_cost_per_hire": 847.32,
      "quality_score": 8.7
    },
    "funnel": {
      "applied": 523,
      "screened": 342,
      "interviewed": 89,
      "offered": 23,
      "hired": 18
    },
    "sources": [
      {
        "source": "LinkedIn",
        "applications": 236,
        "hires": 8,
        "conversion_rate": 3.4
      }
    ]
  }
}
```

### Webhooks

Configure webhooks to receive real-time updates.

#### POST /webhooks
Create a webhook subscription.

**Request:**
```json
{
  "url": "https://yourapp.com/webhooks/hirova",
  "events": [
    "candidate.applied",
    "screening.completed",
    "candidate.status_changed"
  ],
  "secret": "your_webhook_secret"
}
```

**Webhook Payload Example:**
```json
{
  "event": "screening.completed",
  "data": {
    "screening_id": "scr_101",
    "candidate_id": "cand_789",
    "job_id": "job_123",
    "match_score": 92,
    "status": "completed"
  },
  "timestamp": "2024-01-15T10:45:00Z",
  "signature": "sha256=abc123..."
}
```

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Invalid API key |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

## SDKs

Official SDKs are available for:

- JavaScript/TypeScript: `npm install @hirova/sdk`
- Python: `pip install hirova-sdk`
- Ruby: `gem install hirova`
- PHP: `composer require hirova/sdk`

### JavaScript Example

```javascript
import { HirovaClient } from '@hirova/sdk';

const client = new HirovaClient({
  apiKey: 'YOUR_API_KEY'
});

// List jobs
const jobs = await client.jobs.list({
  status: 'active',
  page: 1
});

// Create a job
const job = await client.jobs.create({
  title: 'Frontend Developer',
  department: 'Engineering',
  requirements: {
    required_skills: ['React', 'TypeScript']
  }
});

// Get candidates
const candidates = await client.candidates.list(job.id, {
  min_match_score: 80
});
```

### Python Example

```python
from hirova import HirovaClient

client = HirovaClient(api_key='YOUR_API_KEY')

# List jobs
jobs = client.jobs.list(status='active')

# Create a job
job = client.jobs.create(
    title='Frontend Developer',
    department='Engineering',
    requirements={
        'required_skills': ['React', 'TypeScript']
    }
)

# Get candidates
candidates = client.candidates.list(
    job_id=job.id,
    min_match_score=80
)
```

## Best Practices

1. **Pagination**: Always paginate large result sets
2. **Caching**: Cache frequently accessed data
3. **Error Handling**: Implement exponential backoff for retries
4. **Webhooks**: Use webhooks instead of polling
5. **Rate Limits**: Monitor X-RateLimit headers

### Voice Commands

#### POST /voice/command
Process voice commands for recruiting tasks.

**Request:**
```json
{
  "audio_url": "https://storage.hirova.ai/voice/cmd_123.wav",
  "text": "Find me a senior React developer in San Francisco",
  "source": "alexa"
}
```

**Response:**
```json
{
  "data": {
    "intent": "search_candidates",
    "parameters": {
      "role": "senior React developer",
      "location": "San Francisco"
    },
    "results": {
      "count": 12,
      "top_match": {
        "name": "John Doe",
        "match_score": 94,
        "availability": "immediate"
      }
    },
    "voice_response": "I found 12 senior React developers in San Francisco. The top match is John Doe with a 94% match score."
  }
}
```

### Career Path

#### GET /career-path/{job_id}
Get career path visualization for a specific role.

**Response:**
```json
{
  "data": {
    "current_role": {
      "title": "Senior Frontend Developer",
      "salary_range": {
        "min": 120000,
        "max": 150000
      }
    },
    "progression": [
      {
        "years": "1-2",
        "role": "Tech Lead",
        "salary_range": {
          "min": 150000,
          "max": 180000
        },
        "required_skills": ["Team leadership", "Architecture"],
        "probability": 0.72
      },
      {
        "years": "3-5",
        "role": "Engineering Manager",
        "salary_range": {
          "min": 180000,
          "max": 220000
        },
        "alternate_path": "Principal Engineer"
      }
    ],
    "success_stories": [
      {
        "name": "Sarah Chen",
        "journey": "Frontend Dev → Tech Lead → VP Eng",
        "years": 4
      }
    ]
  }
}
```

## Changelog

### v2.0.0 (2024-06-15)
- AI Interview Coach endpoints
- Skills Gap Analyzer
- Predictive Analytics APIs
- Video Resume Analysis
- Voice Command Support
- Career Path Visualization
- Team Chemistry Predictions
- Blockchain Verification endpoints

### v1.0.0 (2024-01-15)
- Initial API release
- Core endpoints for jobs, candidates, and screening
- Webhook support
- Analytics endpoints

---

*For support, contact api-support@hirova.ai*