from settings import Settings


def test_settings_loaded():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ml-api-test"
    assert settings.API_KEY == "fake-api-key"
