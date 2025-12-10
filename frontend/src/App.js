import React, { useState, useEffect } from 'react';

function App() {
  const [backendStatus, setBackendStatus] = useState('Verificando...');
  const [backendUrl, setBackendUrl] = useState('');

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
    setBackendUrl(apiUrl);

    // Intentar conectarse al backend
    fetch(`${apiUrl}/`)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Error al conectar con el backend');
      })
      .then(data => {
        setBackendStatus('✅ Conectado correctamente');
        console.log('Backend response:', data);
      })
      .catch(error => {
        setBackendStatus('❌ No se pudo conectar al backend');
        console.error('Error connecting to backend:', error);
      });
  }, []);

  return (
    <div style={{
      fontFamily: 'Arial, sans-serif',
      maxWidth: '800px',
      margin: '50px auto',
      padding: '20px',
      textAlign: 'center'
    }}>
      <h1>🤖 AI Development Platform</h1>
      <p style={{ fontSize: '1.2em', color: '#666' }}>
        Bienvenido a la plataforma de desarrollo con IA
      </p>
      
      <div style={{
        marginTop: '40px',
        padding: '20px',
        border: '1px solid #ddd',
        borderRadius: '8px',
        backgroundColor: '#f9f9f9'
      }}>
        <h2>Estado del Backend</h2>
        <p><strong>URL:</strong> {backendUrl}</p>
        <p><strong>Estado:</strong> {backendStatus}</p>
      </div>

      <div style={{
        marginTop: '40px',
        padding: '20px',
        border: '1px solid #ddd',
        borderRadius: '8px',
        backgroundColor: '#f0f8ff'
      }}>
        <h3>Información del Sistema</h3>
        <p><strong>Entorno:</strong> {process.env.NODE_ENV || 'development'}</p>
        <p><strong>React Version:</strong> {React.version}</p>
      </div>
    </div>
  );
}

export default App;
