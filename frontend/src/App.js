import React, { useState, useEffect } from 'react';

function App() {
  const [backendStatus, setBackendStatus] = useState('Checking...');
  const [backendData, setBackendData] = useState(null);
  const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  useEffect(() => {
    // Try to connect to backend health endpoint
    const checkBackend = async () => {
      try {
        const response = await fetch(`${apiUrl}/api/health`);
        if (response.ok) {
          const data = await response.json();
          setBackendStatus('Connected');
          setBackendData(data);
        } else {
          setBackendStatus('Backend responded with error');
        }
      } catch (error) {
        setBackendStatus('Unable to connect to backend');
        console.error('Backend connection error:', error);
      }
    };

    checkBackend();
    // Check every 10 seconds
    const interval = setInterval(checkBackend, 10000);
    return () => clearInterval(interval);
  }, [apiUrl]);

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1 style={styles.title}>AI Development Platform</h1>
        <p style={styles.subtitle}>Frontend Application</p>
      </header>
      
      <main style={styles.main}>
        <div style={styles.card}>
          <h2 style={styles.cardTitle}>Backend Connection Status</h2>
          <div style={styles.statusContainer}>
            <span style={styles.label}>Status:</span>
            <span style={{
              ...styles.status,
              color: backendStatus === 'Connected' ? '#4caf50' : '#f44336'
            }}>
              {backendStatus}
            </span>
          </div>
          <div style={styles.statusContainer}>
            <span style={styles.label}>API URL:</span>
            <span style={styles.value}>{apiUrl}</span>
          </div>
          {backendData && (
            <div style={styles.backendInfo}>
              <h3 style={styles.infoTitle}>Backend Information</h3>
              <div style={styles.infoItem}>
                <span style={styles.label}>Service:</span>
                <span style={styles.value}>{backendData.service}</span>
              </div>
              <div style={styles.infoItem}>
                <span style={styles.label}>Version:</span>
                <span style={styles.value}>{backendData.version}</span>
              </div>
              <div style={styles.infoItem}>
                <span style={styles.label}>Status:</span>
                <span style={styles.value}>{backendData.status}</span>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

const styles = {
  container: {
    minHeight: '100vh',
    backgroundColor: '#f5f5f5',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif',
  },
  header: {
    backgroundColor: '#282c34',
    padding: '2rem',
    color: 'white',
    textAlign: 'center',
  },
  title: {
    margin: 0,
    fontSize: '2.5rem',
    fontWeight: 'bold',
  },
  subtitle: {
    margin: '0.5rem 0 0 0',
    fontSize: '1.2rem',
    color: '#61dafb',
  },
  main: {
    padding: '2rem',
    display: 'flex',
    justifyContent: 'center',
  },
  card: {
    backgroundColor: 'white',
    borderRadius: '8px',
    padding: '2rem',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
    maxWidth: '600px',
    width: '100%',
  },
  cardTitle: {
    margin: '0 0 1.5rem 0',
    fontSize: '1.5rem',
    color: '#333',
  },
  statusContainer: {
    display: 'flex',
    marginBottom: '1rem',
    alignItems: 'center',
  },
  label: {
    fontWeight: 'bold',
    marginRight: '0.5rem',
    color: '#666',
  },
  status: {
    fontSize: '1.1rem',
    fontWeight: 'bold',
  },
  value: {
    color: '#333',
  },
  backendInfo: {
    marginTop: '2rem',
    paddingTop: '1.5rem',
    borderTop: '1px solid #e0e0e0',
  },
  infoTitle: {
    margin: '0 0 1rem 0',
    fontSize: '1.2rem',
    color: '#333',
  },
  infoItem: {
    display: 'flex',
    marginBottom: '0.5rem',
  },
};

export default App;
