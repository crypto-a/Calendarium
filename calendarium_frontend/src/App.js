import logo from './logo.svg';
import './App.css';
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Home from './components/Pages/Home/Home';
import Navbar from './components/Navbar/Navbar';


function App() {
  return (
    
    <Router>
      <Navbar>
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/pricing' component={Home} />
        <Route path='/aboutus' component={Home} />
        <Route path='/contact-us' component={Home} />
      </Switch>
    </Navbar>
    </Router>
  );
}

export default App;
