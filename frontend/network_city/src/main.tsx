import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css'

import { Header } from "@/components/header/Header";

import Groups from "@/pages/groups/Groups";

createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <BrowserRouter>
            <Header />

            <Routes>
                <Route path="/" element={<Groups />} />
            </Routes>
        </BrowserRouter>
    </StrictMode>,
)
