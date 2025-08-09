import { useState } from 'react';

export default function Home() {
  const [profile, setProfile] = useState({ name: '', role: '', industry: '', interests: '' });
  const [post, setPost] = useState('');

  const generatePost = async () => {
    const res = await fetch('/api/generate', {
      method: 'POST',
      body: JSON.stringify(profile),
      headers: { 'Content-Type': 'application/json' }
    });
    const data = await res.json();
    setPost(data.post);
  };

  return (
    <div>
      <h1>LinkedIn AI Agent</h1>
      <input placeholder="Name" onChange={e => setProfile({ ...profile, name: e.target.value })} />
      <input placeholder="Role" onChange={e => setProfile({ ...profile, role: e.target.value })} />
      <input placeholder="Industry" onChange={e => setProfile({ ...profile, industry: e.target.value })} />
      <input placeholder="Interests (comma-separated)" onChange={e => setProfile({ ...profile, interests: e.target.value.split(',') })} />
      <button onClick={generatePost}>Generate Post</button>
      <p>{post}</p>
    </div>
  );
}
