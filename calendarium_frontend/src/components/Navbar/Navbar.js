import React, { Component } from 'react';
import { useState } from 'react';
import '../../App.css'
import { menuItems } from './Menuitems.js';
import './Navbar.css'


function Navbar() {
    const [clicked, setClicked] = useState(false)
    return (
        <nav className="navbar-container">
        <h1 className="navbar-logo">Calendarium</h1>

        <div className="navbar-menu-btn" onClick={() => (setClicked(!clicked))}>
            <br/>
        </div>

        <ul className={clicked ? "nav-menu active" : "nav-menu"}>
            {menuItems.map((item, index) => {
                    return(
                    <li key={index}>
                        <a className={item.cName} href={item.url}>
                            {item.title}
                        </a>
                    </li>
                )})}
        </ul>
    </nav>
    );
  }

export default Navbar;