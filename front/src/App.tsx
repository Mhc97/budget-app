import React, { useEffect, useState } from 'react';
import Footer from './component/Footer';

interface Expense {
  id: number;
  title: string;
  amount: number;
  category: string;
}

// interface SubmitEvent<T = Event>

function App() {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');

  const API_URL = 'http://localhost:8000';

  useEffect(() => {
    fetch(`${API_URL}/expenses`)
      .then(response => {
        if (!response.ok) throw new Error('Erreur_API');        
        return response.json();
      })
      .then(data => {
        setExpenses(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);


// Ajouter une dépense
  const addExpense = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch(`${API_URL}/expenses`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title,
          amount: parseFloat(amount),
          category,
        }),
      });
    if (!response.ok) throw new Error('Erreur création');
    const newExpense = await response.json();
    setExpenses([...expenses, newExpense]);
    setAmount('');
    setTitle('');
    setAmount('');
    setCategory('');
  }catch (err) {
    setError(err instanceof Error ? err.message : `Erreur`);
  }
};

// Supprimer une dépense
const deleteExpenses = async (id: number) => {
  try {
    const response = await fetch(`${API_URL}/expenses/${id}`,{
      method: 'DELETE',
    });
    if (!Response.ok) throw new Error(`Erreur suppression`);
    setExpenses(expenses.filter(e => e.id !== id));
  } catch (err) {
    setError(err instanceof Error ? err.message : 'Erreur');
  }
};  

  if (loading) return <div>Chargement... </div>;
  if (error) return <div>Erreur : {error}</div>;

  return (
  <>
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>💰 Budget App</h1>
      <h2>Listes des dépenses</h2>
      <ul>
        {expenses.map(expense => (
          <li key={expense.id}>
            <strong>{expense.title}</strong> : {expense.amount}€ ({expense.category})
          </li>
        ))}
      </ul>
    </div>
    <Footer/>
    </>
  );
}

export default App;