import React, {useContext} from 'react';
import Navbar from '../../../components/Navbar';
import Footer from '../../../components/Footer';
import SearchFilter from './SearchFilter';
import { UserContext } from '../../../context/UserContext';

const StudentSearch = () => {  
    const { user, userLogout } = useContext(UserContext);
    return (
        <div className="flex flex-col justify-between min-h-screen dark:bg-gray-900">
            <Navbar  user={user} onLogout={userLogout}/>
            <SearchFilter />
            <Footer />
        </div>

    );
};

export default StudentSearch;