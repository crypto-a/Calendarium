import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Home from './components/Pages/Home/Home';
function App() {
  return (
    
    <Router>
      <Switch>
        <Route path="/" exact component={Home}></Route>
      </Switch>
    </Router>
  );
}

export default App;
