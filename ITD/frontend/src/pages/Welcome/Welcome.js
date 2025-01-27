import React, {useContext} from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import JumboTron from './JumboTron';
import SocialProof from './SocialProof';
import WhoTrustUs from './WhoTrustUs';
import { Box } from "@mui/material";  
import { UserContext } from '../../context/UserContext';

const Welcome = () => {
  const { user, userLogout } = useContext(UserContext);
  return (
    <Box>
      <Navbar user={user} onLogout={userLogout} />
      <JumboTron/>
      <SocialProof/>
      <WhoTrustUs/>
      <Footer/>
    </Box>
  );
};

export default Welcome;