from unittest.mock import AsyncMock, MagicMock

@pytest.mark.asyncio
async def test_send_markdown_email(mocker, email_service):
    mocker.patch.object(email_service.smtp_client, "send_email", return_value=None)
    
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123",
        "verification_token": "abc123"
    }

    await email_service.send_user_email(user_data, 'email_verification')
    # Manual verification in Mailtrap
