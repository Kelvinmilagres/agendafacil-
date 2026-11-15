## O que muda e por quê
<!-- Descreva em poucas linhas. Cite a história (H..), regra (RN..) ou ADR relacionados. -->

## Checklist do revisor (Template 18)
- [ ] O código está no módulo certo e não cria dependência proibida (ver docs/adr/ADR-002.md)
- [ ] O segredo de cada módulo continua escondido
- [ ] Há teste para a regra criada ou alterada (partições, valores-limite, erros)
- [ ] Os testes não dependem de ordem, relógio real, rede ou recurso de produção
- [ ] O pipeline passou
- [ ] Sem senhas, chaves ou dados reais; sem código comentado
- [ ] O PR é pequeno e o ADR foi atualizado, se a decisão mudou
