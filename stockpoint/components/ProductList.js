// components/ProductList.js
import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, ActivityIndicator, StyleSheet } from 'react-native';

const getData = async () => {
  try {
    const response = await fetch('http://ec2-3-87-211-227.compute-1.amazonaws.com/api/produtos/');
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Failed to fetch data', error);
    throw error;
  }
};

const ProductList = () => {
  const [produtos, setProdutos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await getData();
        setProdutos(result);
      } catch (error) {
        setError('Não foi possível carregar os produtos');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <ActivityIndicator style={styles.loader} size="large" color="#0000ff" />;
  }

  if (error) {
    return (
      <View style={styles.center}>
        <Text>{error}</Text>  {}
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <FlatList
        data={produtos}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.productItem}>
            <Text>ID: {item.id}</Text>
            <Text>Título: {item.title}</Text>
            <Text>Categoria: {item.categoria}</Text>
            <Text>Marca: {item.marca}</Text>
            <Text>Preço de Custo: R$ {item.cost_price}</Text>
            <Text>Preço de Venda: R$ {item.selling_price}</Text>
            <Text>Número de Série: {item.serie_number}</Text>
            <Text>Quantidade: {item.quantity}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 10,
  },
  loader: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  productItem: {
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
});

export default ProductList;
