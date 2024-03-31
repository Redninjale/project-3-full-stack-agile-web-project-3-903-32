import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';

const Menu = () => {
  const [menuItems, setMenuItems] = useState([]);
  const [menuModal, setMenuModal] = useState(false);
  const [menuName, setMenuName] = useState('');
  const [menuPrice, setMenuPrice] = useState('');
  const [menuId, setMenuId] = useState('');
  const [itemInventoryList, setItemInventoryList] = useState([]);
  const [itemOutsideInventoryList, setItemOutsideInventoryList] = useState([]);

  useEffect(() => {
    getMenu();
  }, []);

  const handleAddMenu = (event) => {
    event.preventDefault();
    setMenuId('');
    setMenuName('');
    setMenuPrice('');
    setMenuModal(true);
  }

  const handleAddItem = (event) => {
    event.preventDefault();
    if (document.getElementById('newItemAmount').value !== '' 
    && document.getElementById('newItemSelect').value !== '') {
      document.getElementById('newItemAmount').value = parseFloat(document.getElementById('newItemAmount').value).toFixed(2);
      postMenuInventory(menuId);
    }
  }

  const handleDeleteItem = (event) => {
    event.preventDefault();
    deleteMenuInventory(menuId, event.target.id);
  }

  const handleEditItem = (event) => {
    event.preventDefault();
    setMenuId(menuItems[event.target.id].id);
    setMenuName(menuItems[event.target.id].itemName);
    setMenuPrice(menuItems[event.target.id].price);
    getMenuInventory(menuItems[event.target.id].id);
    getOutsideMenuInventory(menuItems[event.target.id].id);
    setMenuModal(true);
  }

  const handleChangeAmount = (index, event) => {
    // 13 is the keycode for enter
    if (event.keyCode === 13) {
      document.getElementsByName('editItemAmount')[index].value = parseFloat(document.getElementsByName('editItemAmount')[index].value).toFixed(2);
      itemInventoryList[index].itemAmount = document.getElementsByName('editItemAmount')[index].value;
      putMenuInventory(menuId, index);
    }
  }

  async function getMenu() {
    try {
      const response = await fetch(process.env.REACT_APP_BACKEND_URL + "/api/menu", {
        method: "GET",
        mode: 'cors'
      });
      if (response.ok) {
        const data = await response.json();
        setMenuItems(data);
      } else {
        console.error('Failed to fetch menu:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error fetching menu:', error);
    }
  }

  async function getMenuInventory(menu_id) {
    try {
      const response = await fetch(process.env.REACT_APP_BACKEND_URL + "/api/mijunc/" + menu_id, {
        method: "GET",
        mode: 'cors'
      });
      if (response.ok) {
        const data = await response.json();
        setItemInventoryList(data);
      } else {
        console.error('Failed to fetch menu:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error fetching menu:', error);
    }
  }

  async function postMenuInventory(menu_id) {
    try {
      const selectedItemId = document.getElementById('newItemSelect').value;
      const selectedAmount = document.getElementById('newItemAmount').value;
      const response = await fetch(process.env.REACT_APP_BACKEND_URL + "/api/mijunc/" + menu_id, {
        method: "POST",
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "itemID" : selectedItemId, "itemAmount": selectedAmount})
      });
      if (response.ok) {
        getMenuInventory(menu_id);
        getOutsideMenuInventory(menu_id);
      } else {
        console.error('Failed to fetch menu:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error fetching menu:', error);
    }
  }

  async function deleteMenuInventory(menu_id, index) {
    try {
      const response = await fetch(process.env.REACT_APP_BACKEND_URL + "/api/mijunc/" + menu_id, {
        method: "DELETE",
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "itemID" : itemInventoryList[index].itemID })
      });
      if (response.ok) {
        getMenuInventory(menu_id);
      } else {
        console.error('Failed to delete menu inventory:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error deleting menu inventory:', error);
    }
  }

  async function putMenuInventory(menu_id, index) {
    try {
      const response = await fetch(process.env.REACT_APP_BACKEND_URL + "/api/mijunc/" + menu_id, {
        method: "PUT",
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "itemID" : itemInventoryList[index].itemID, "itemAmount": itemInventoryList[index].itemAmount})
      });
      if (response.ok) {
        getMenuInventory(menu_id);
      } else {
        console.error('Failed to fetch menu:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error fetching menu:', error);
    }
  }

  async function getOutsideMenuInventory(menu_id) {
    try {
      // console.log(menu_id);
      const response = await fetch(process.env.REACT_APP_BACKEND_URL + "/api/mijunc/outside/" + menu_id, {
        method: "GET",
        mode: 'cors'
      });
      if (response.ok) {
        const data = await response.json();
        setItemOutsideInventoryList(data);
      } else {
        console.error('Failed to fetch menu:', response.status, response.statusText);
      }
    } catch (error) {
      console.error('Error fetching menu:', error);
    }
  }

  const Modal = () => (
    (<div className='absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-gray-400 flex flex-col'>
    <div className='p-4'>
      <label htmlFor='item_name'>Item Name:</label>
      <input type='text' name='item_name' value={menuName} onChange={(e) => setMenuName(e.target.value)} />
      <label htmlFor='item_price'>Item Price:</label>
      <input type='text' name='item_price' value={menuPrice} onChange={(e) => setMenuPrice(e.target.value)} />
    </div>
    <table>
      <thead>
        <tr>
          <th>Inventory Name</th>
          <th>Amount</th>
        </tr>
      </thead>
      <tbody>
        {
          itemInventoryList.map((item, index) => (
            <tr key={index}>
              <td>{item.itemName}</td>
              <td><input type="number" name='editItemAmount' defaultValue={item.itemAmount} onKeyDown={e => handleChangeAmount(index, e)} /></td>
            </tr>
          ))
        }
        <tr>
          <td>
            <select id='newItemSelect'>
              {
                itemOutsideInventoryList.map((item, index) => (
                  <option key={index} value={item.itemID}>{item.itemName}</option>
                ))
              }
            </select>
          </td>
          <td>
            <label htmlFor='inventory_amount'>Inventory Amount:</label>
            <input type='number' id='newItemAmount'/>
          </td>
        </tr>
      </tbody>
    </table>
    <div className='p-4'>
      <button onClick={handleAddItem}>Add</button>
    </div>
  </div>)
  )

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col overflow-hidden">
        <header className="flex justify-between items-center p-6 bg-white border-b border-gray-200">
          <h1 className="text-xl font-semibold text-gray-700">Menu</h1>
        </header>
        <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200 p-6">
          <table className="min-w-full bg-white">
            <thead>
              <tr>
                <th className="border-b-2 p-4 text-left text-base font-semibold text-gray-600 uppercase tracking-wider">
                  Item Name
                </th>
                <th className="border-b-2 p-4 text-left text-base font-semibold text-gray-600 uppercase tracking-wider">
                  Price
                </th>
                <th>
                  Edit
                </th>
              </tr>
            </thead>
            <tbody>
              {menuItems.map((item, index) => (
                <tr key={index} className="bg-white border-b">
                  <td className="p-4 text-base text-gray-700">{item.itemName}</td>
                  <td className="p-4 text-base text-gray-700">${item.price}</td>
                  <td className="p-4 text-base text-gray-700"><button id={index} onClick={handleEditItem}>Edit</button></td>
                </tr>
              ))}
              <tr key={-1} className="bg-white border-b" onClick={handleAddItem}>
                <td className="text-center w-full text-base border-gray-700 border-dotted border-2 border-r-0 text-gray-700"><button className='text-2xl p-4 w-full'>+</button></td>
                <td className="text-center w-full text-base border-gray-700 border-dotted border-2 border-l-0 text-gray-700"><button className='text-2xl p-4 w-full'></button></td>
              </tr>
            </tbody>
          </table>
          {
            menuModal &&
            <Modal />
          }
        </main>
      </div>
    </div>
  );
};

export default Menu;