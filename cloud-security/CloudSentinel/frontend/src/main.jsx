import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import keycloak from "./auth/keycloak";
import "./styles.css";

async function bootstrap() {
  try {
    const authenticated = await keycloak.init({
      onLoad: "login-required",
      pkceMethod: "S256",
      checkLoginIframe: false,
    });

    if (!authenticated) {
      await keycloak.login();
      return;
    }

    createRoot(document.getElementById("root")).render(
      <React.StrictMode><App /></React.StrictMode>
    );
  } catch (error) {
    console.error("Keycloak initialization failed:", error);
    document.getElementById("root").innerHTML =
      '<div style="padding:40px;font-family:Arial;color:#dce8f5;background:#07111f;min-height:100vh"><h2>CloudSentinel Identity unavailable</h2><p>Start Keycloak at http://localhost:8080 and refresh this page.</p></div>';
  }
}

bootstrap();
