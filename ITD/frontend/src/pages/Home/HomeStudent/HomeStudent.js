import React from 'react';
import { Link } from 'react-router-dom';

const HomeStudent = () => {
    return (
        <div>
            <h1>Welcome to the Student Home Page</h1>
            <p>Thank you for registering with us.</p>
            <nav>
                <ul>
                    <li><Link to="/dashboard">Go to Dashboard</Link></li>
                    <li><Link to="/profile">View Profile</Link></li>
                    <li><Link to="/settings">Account Settings</Link></li>
                </ul>
            </nav>
        </div>
    );
};

export default HomeStudent;