# Email Validation Services

This document contains information about email validation services that are used or planned to be used in the validation modules.

## Existing Integrations

### 1. NeverBounce

- **System Name**: `neverbounce`
- **API URL**: `https://api.neverbounce.com/v4/single/check`
- **Request Parameters**:
  - `key` - API key
  - `email` - email address to verify
- **API Version**: v4
- **Documentation**: [NeverBounce API Documentation](https://developers.neverbounce.com/docs/single-check)
- **Description**: Service for checking email address validity. Verifies syntax, domain, MX records, and mailbox existence.
- **Pricing**: From $0.003 per check, depending on volume.
- **Features**: High accuracy, speed, bulk verification capability.

### 2. QuickEmailVerification

- **System Name**: `quickemailverification`
- **API URL**: `https://api.quickemailverification.com/v1/verify`
- **Request Parameters**:
  - `apikey` - API key
  - `email` - email address to verify
- **API Version**: v1
- **Documentation**: [QuickEmailVerification API Documentation](https://www.quickemailverification.com/docs/email-verification-api)
- **Description**: Service for checking email addresses with high accuracy. Verifies syntax, domain, MX records, SMTP connection.
- **Pricing**: From $0.002 per check, depending on volume.
- **Features**: High accuracy, speed, detailed verification result information.

### 3. MillionVerifier

- **System Name**: `millionverifier`
- **API URL**: `https://api.millionverifier.com/api/v3`
- **Request Parameters**:
  - `api` - API key
  - `email` - email address to verify
  - `timeout` - wait time (10 seconds)
- **API Version**: v3
- **Documentation**: [MillionVerifier API Documentation](https://millionverifier.com/api-documentation/)
- **Description**: Service for checking email addresses with high accuracy. Verifies syntax, domain, MX records, SMTP connection.
- **Pricing**: From $0.001 per check, depending on volume.
- **Features**: High accuracy, speed, bulk verification capability.

## Implemented Integrations

### 1. SendPulse

- **System Name**: `sendpulse`
- **API URL**: `https://api.sendpulse.com/verifier`
- **Request Parameters**:
  - `api_user_id` - API user ID
  - `api_secret` - API secret key
  - `email` - email address to verify
- **API Version**: v1
- **Website**: [SendPulse](https://sendpulse.com)
- **Documentation**: [SendPulse API Documentation](https://sendpulse.com/integrations/api/verifier)
- **Description**: Service for email verification and mass mailings. Verifies syntax, domain, MX records, SMTP connection.
- **Pricing**: From $0.002 per check, depending on volume.
- **Features**: Integration with other SendPulse services, bulk verification capability.

### 2. ZeroBounce

- **System Name**: `zerobounce`
- **API URL**: `https://api.zerobounce.net/v2/validate`
- **Request Parameters**:
  - `api_key` - API key
  - `email` - email address to verify
  - `ip_address` - optional, IP address of the sender
- **API Version**: v2
- **Website**: [ZeroBounce](https://www.zerobounce.net)
- **Documentation**: [ZeroBounce API Documentation](https://www.zerobounce.net/docs/email-validation-api-quickstart/)
- **Description**: Service for checking email addresses with high accuracy. Verifies syntax, domain, MX records, SMTP connection.
- **Pricing**: From $0.002 per check, depending on volume.
- **Features**: High accuracy, speed, detailed verification result information, AI-scoring.


### 3. Clearout

- **System Name**: `clearout`
- **API URL**: `https://api.clearout.io/v2/email_verify/instant`
- **Request Parameters**:
  - `api_key` - API key
  - `email` - email address to verify
- **API Version**: v2
- **Website**: [Clearout](https://clearout.io)
- **Documentation**: [Clearout API Documentation](https://docs.clearout.io/email-verifier-api.html)
- **Description**: Service for checking email addresses with high accuracy and speed. Verifies syntax, domain, MX records, SMTP connection and spam traps.
- **Pricing**: From $0.003 per check, depending on volume.
- **Features**: High accuracy, spam trap detection, detailed verification result information.

### 4. MailerCheck

- **System Name**: `mailercheck`
- **API URL**: `https://api.mailercheck.com/v1/verify/single`
- **Request Parameters**:
  - `api_key` - API key
  - `email` - email address to verify
- **API Version**: v1
- **Website**: [MailerCheck](https://www.mailercheck.com/)
- **Documentation**: [MailerCheck API Documentation](https://developers.mailercheck.com/)
- **Description**: Service for checking email addresses with high accuracy. Verifies syntax, domain, MX records, SMTP connection and spam traps.
- **Pricing**: From $0.002 per check, depending on volume.
- **Features**: High accuracy, spam trap detection, detailed verification result information.

### 5. Mailgun

- **System Name**: `mailgun`
- **API URL**: `https://api.mailgun.net/v4/address/validate`
- **Request Parameters**:
  - `api_key` - API key
  - `address` - email address to verify
- **API Version**: v4
- **Website**: [Mailgun](https://www.mailgun.com/)
- **Documentation**: [Mailgun API Documentation](https://help.mailgun.com/hc/en-us/articles/360010523074-Email-Validations)
- **Description**: Service for checking email addresses with high accuracy. Verifies syntax, domain, MX records, SMTP connection and spam traps.
- **Pricing**: From $0.001 per check, depending on volume.
- **Features**: High accuracy, integration with other Mailgun services, bulk verification capability.

## Service Comparison

| Service | Accuracy | Speed | Price (per 1000) | Bulk Verification | AI-scoring | Spam Trap Detection |
|--------|----------|-----------|----------------|------------------|------------|----------------|
| NeverBounce | High | High | $3.00 | Yes | No | Partial |
| QuickEmailVerification | High | High | $2.00 | Yes | No | Partial |
| MillionVerifier | Medium | High | $1.00 | Yes | No | No |
| SendPulse | Medium | Medium | $2.00 | Yes | No | No |
| ZeroBounce | High | High | $2.00 | Yes | Yes | Yes |
| Clearout | High | High | $3.00 | Yes | No | Yes |
| MailerCheck | High | High | $2.00 | Yes | No | Yes |
| Mailgun | High | High | $1.00 | Yes | No | Yes |

## Service Selection Recommendations

1. **For small verification volumes**: ZeroBounce or Clearout - high accuracy but higher price.
2. **For large verification volumes**: Mailgun or MillionVerifier - lower price, acceptable accuracy.
3. **For integration with other services**: 
   - SendPulse - if you already use other SendPulse services.
   - Mailgun - if you already use Mailgun services for email sending.
4. **For highest accuracy**: ZeroBounce with AI-scoring.
5. **For spam trap detection**: Clearout, MailerCheck or Mailgun - have advanced spam trap detection capabilities.
6. **For optimal price/quality ratio**: MailerCheck or Mailgun - high accuracy at a reasonable price.
