import React from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import JumboTron from './JumboTron';
import SocialProof from './SocialProof';
import WhoTrustUs from './WhoTrustUs';
import { Box } from "@mui/material";  

const Welcome = () => {
  return (
    <Box>
      <Navbar/>
      <JumboTron/>
      <SocialProof/>
      <WhoTrustUs/>
      <Footer/>
    </Box>
  );
};

export default Welcome;