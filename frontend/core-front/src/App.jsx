import { router } from './routers/MyRoutes';
import { RouterProvider } from 'react-router-dom';

function App() {

  return (
    <RouterProvider router={router()}/>
  )
}

export default App;
