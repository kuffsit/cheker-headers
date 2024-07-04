import requests

def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Проверка наличия заголовков безопасности
        security_headers = {
            'Content-Security-Policy': "Content-Security-Policy",
            'X-Content-Type-Options': "nosniff",
            'X-Frame-Options': "DENY",
            'Strict-Transport-Security': "max-age=31536000; includeSubDomains",
            'X-XSS-Protection': "1; mode=block",
            'Referrer-Policy': "no-referrer",
            'Permissions-Policy': "interest-cohort=()"
        }

        missing_headers = []
        incorrect_headers = []

        for header, expected_value in security_headers.items():
            if header not in headers:
                missing_headers.append(header)
            elif headers[header] != expected_value:
                incorrect_headers.append((header, headers[header]))

        if missing_headers:
            print(f"Missing security headers for {url}:")
            for header in missing_headers:
                print(f"- {header}")
        else:
            print(f"All security headers are present for {url}.")

        if incorrect_headers:
            print(f"Headers with incorrect values for {url}:")
            for header, actual_value in incorrect_headers:
                print(f"- {header}: {actual_value} (expected: {security_headers[header]})")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

# Пример использования
if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    check_headers(url)

